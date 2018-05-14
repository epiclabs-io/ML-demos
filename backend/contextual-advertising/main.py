import sys
import os
import tensorflow as tf
import numpy as np
from PIL import Image
import operator
import re
import json
import youtube_dl
import argparse
import redis
from threading import Thread

real_path = os.path.realpath(__file__)
base_dir = real_path[:real_path.rfind("/")]
sys.path.append(base_dir + '/..')

from flask import Flask
from flask import request
from flask import Response
from flask import send_from_directory, send_file
from datasets import imagenet
from nets import inception_resnet_v2
from amazonapi import *


parser = argparse.ArgumentParser(description='Detect relevant tags in a YouTube video.')
parser.add_argument('-f', '--fps', default='2', help='Number of thumbnails per second that will be analyzed from the video')
args = parser.parse_args()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress tensorflow's compilation warnings

app = Flask(__name__)

# Create and clean tmp
if not os.path.exists("tmp"):
    os.makedirs("tmp")

for elem in os.listdir("tmp/"):
    if elem:
        os.remove("tmp/" + elem)

if not os.path.exists("static/video"):
    os.makedirs("static/video")

if not os.path.exists("static/video/tmp"):
    os.makedirs("static/video/tmp")

# Delete temp videos
for elem in os.listdir("static/video/tmp/"):
    if elem:
        os.remove("static/video/tmp" + elem)

fps = args.fps
global semaphore
semaphore = False
# Start and clean Redis server
tag_buffer_db = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
tag_to_banner_db = redis.StrictRedis(host='localhost', port=6379, db=1, decode_responses=True)
total_tags = redis.StrictRedis(host='localhost', port=6379, db=2, charset="utf-8", decode_responses=True)
summary = redis.StrictRedis(host='localhost', port=6379, db=3, charset="utf-8", decode_responses=True)
tag_buffer_db.flushdb()
tag_to_banner_db.flushdb()
total_tags.flushdb()
summary.flushdb()

checkpoint_file = 'vol/inception_resnet_v2_2016_08_30.ckpt'

# Load and Prepare Graph from checkpoint file
slim = tf.contrib.slim
image_size = 299
names = imagenet.create_readable_names_for_imagenet_labels()

input_tensor = tf.placeholder(tf.float32, shape=(None, 299, 299, 3), name='input_image')
sess = tf.Session()
arg_scope = inception_resnet_v2.inception_resnet_v2_arg_scope()

with slim.arg_scope(arg_scope):
    logits, end_points = inception_resnet_v2.inception_resnet_v2(input_tensor, is_training=False)

print("------ The Graph is ready ------")


saver = tf.train.Saver()
saver.restore(sess, checkpoint_file)
beta = 0.85
penalty = 0.01
num_tags = 20


def number_key(name):
    parts = re.findall('[^0-9]+|[0-9]+', name)
    l = []
    for part in parts:
        try:
            l.append(int(part))
        except ValueError:
            l.append(part)
    return l


def clear_tmp_images():
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    for img in os.listdir("tmp/"):
        if img:
            os.remove("tmp/" + img)


def classify_image(image_path):
    im = Image.open(image_path).resize((299, 299))
    im = np.array(im)
    im = im.reshape(-1, 299, 299, 3)
    probabilities, _ = sess.run([end_points['Predictions'], logits], feed_dict={input_tensor: 2*(im/255.0)-1.0})
    probabilities = probabilities[0]
    sorted_probabilities = sorted(probabilities, reverse=True)
    for i in range(num_tags):
        index = np.where(probabilities == sorted_probabilities[i])
        tag = names[index[0][0]].replace("\'", "")
        tmp_tag = re.split(',+', tag)
        if len(tmp_tag) > 2:
            tag = tmp_tag[0] + ',' + tmp_tag[1]
        prob = probabilities[index[0][0]]
        if tag in total_tags.keys():
            last_prob = float(total_tags.get(tag))
            total_tags.set(tag, (1 / beta) * ((beta * last_prob) + ((1 - beta) * prob)))
            summary.set(tag, float(summary.get(tag)) + prob)
        else:
            total_tags.set(tag, (1 / beta) * penalty * prob)
            summary.set(tag, prob)
    tmp_tags = {}
    for tag in total_tags.keys():
        tmp_score = float(total_tags.get(tag)) * beta
        total_tags.set(tag, tmp_score)
        tmp_tags[tag] = tmp_score
    sorted_tags = sorted(tmp_tags.items(), key=operator.itemgetter(1), reverse=True)
    response = []
    for element in sorted_tags[:num_tags]:
        response.append({"text": element[0], "weight": "{0:.6f}".format(element[1])})
    banners = []
    for j in range(3):
        main_tag = re.split(',', response[j]["text"])[0]
        if tag_to_banner_db.exists(main_tag):
            banner = json.loads(tag_to_banner_db.get(main_tag))
        else:
            amazon_response = get_direct_item(main_tag)
            banner = get_url_image_price(amazon_response, directSearch=True)
            tag_to_banner_db.set(main_tag, json.dumps(banner))
        banners.append(banner)
    return response, banners


@app.route('/api/v1/processVideo', methods=['POST'])
def handle_url():
    global semaphore
    semaphore = False
    tag_buffer_db.flushdb()
    summary.flushdb()
    total_tags.flushdb()
    clear_tmp_images()
    video_url = request.json['video']
    video_name = video_url[video_url.rfind('?v=') + 3:]
    app.config['video'] = video_name + '.mp4'
    cached = False
    # Download Youtube video if not cached
    for video in os.listdir('static/video/'):
        if video[:video.rfind(".")] == video_name:
            print("------ The video is already cached ------")
            cached = True
    if not cached:
        download_video(video_url, {'outtmpl': 'static/video/tmp/video.%(format)s', 'format': 'mp4[height<=720p]'})
        video_tmp = os.listdir("static/video/tmp/")[0]
        os.rename("static/video/tmp/" + video_tmp, "static/video/tmp/video.mp4")
        if os.listdir("static/video/tmp")[0] != "video.mp4":
            os.system("ffmpeg -i static/video/tmp/" + video_tmp + ".mp4 -vcodec copy -acodec copy static/video/"
                      + video_name + ".mp4")
        else:
            os.rename("static/video/tmp/video.mp4", "static/video/" + video_name + ".mp4")
    classification_thread = Thread(target=start_classification, args=())
    classification_thread.start()
    ffmpeg_thread = Thread(target=get_frames(video_name, args.fps), args=())
    ffmpeg_thread.start()
    return Response(json.dumps(app.config['video']), mimetype="application/json")


def start_classification():
    print("-------- Starting classification --------")
    i = 0
    while not semaphore or len(os.listdir("tmp")) > 0:
        data = sorted(os.listdir("tmp"), key=number_key)
        if len(data):
            image_path = data[0]
            response, banner = classify_image("tmp/" + image_path)
            time_stamp = (i / float(fps))
            if not tag_buffer_db.set(i, json.dumps({'time': "{0:.4f}".format(time_stamp), 'tags': response,
                                                    'banner': banner})):
                print("An error occurred and the dictionary could not be saved")
            os.remove("tmp/" + image_path)
            i += 1
    global semaphore
    semaphore = False
    print("All images classified")


@app.route("/api/v1/returnClassification", methods=['POST'])
def return_classification():
    response = {}
    scores = []
    for key in tag_buffer_db.keys():
        tag = tag_buffer_db.get(key)
        scores.append(json.loads(tag))
        tag_buffer_db.delete(key)
    response['scores'] = scores
    response['classification'] = semaphore
    return Response(json.dumps(response).replace("\'", "\""), mimetype="application/json")


@app.route('/api/v1/returnSummary', methods=['GET'])
def return_summary():
    total_tags_to_order = {}
    for tag in summary.keys():
        total_tags_to_order[tag] = "{0:.6f}".format(float(summary.get(tag)))
    sorted_tags = sorted(total_tags_to_order.items(), key=operator.itemgetter(1), reverse=True)
    summary_tags = []
    for j in range(3):
        summary_tags.append(json.loads(tag_to_banner_db.get(re.split(',', sorted_tags[j][0])[0])))
    return Response(json.dumps(summary_tags))


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/static/videos/<path:path>')
def send_video(path):
    return send_from_directory('static/video', path)


def download_video(video_url, ydl_opts):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


def get_frames(video_name, fps):
    os.system("ffmpeg -i static/video/" + video_name + ".mp4 -vf fps=" + fps + " -q:v 1 " + "tmp/%06d.jpg")
    global semaphore
    semaphore = True


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6006, threaded=True)
