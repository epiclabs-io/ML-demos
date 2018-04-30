import os
import argparse
import youtube_dl
import redis
import re
import json
import time

real_path = os.path.realpath(__file__)
base_dir = real_path[:real_path.rfind("/")]
from flask import Flask
from flask import request
from flask import Response
from flask import render_template, send_from_directory
from dragon_model import dragon_model
from inception_model import InceptionModel
from threading import Thread
from shutil import copyfile
from time import gmtime, strftime
import csv

parser = argparse.ArgumentParser(description="Alerts if the video has smokers.")
parser.add_argument('-f', '--fps', default='2', help='Number of thumbnails per second that will be analyzed from the video')
parser.add_argument('-t', '--test', action='store_true', help='Test mode flag')
parser.add_argument('-i', '--inception', action='store_true', help='If this flag is active an inception model will be used'
                                                                   'instead of our own model.')
args = parser.parse_args()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress tensorflow's compilation warnings

app = Flask(__name__)

# Create and clean tmp
if not os.path.exists("tmp"):
    os.makedirs("tmp")

if not os.path.exists("static/video"):
    os.makedirs("static/video")

if not os.path.exists("static/video/tmp"):
    os.makedirs("static/video/tmp")

for elem in os.listdir("tmp/"):
    if elem:
        os.remove("tmp/" + elem)

# Delete temp videos
for elem in os.listdir("static/video/tmp/"):
    if elem:
        os.remove("static/video/tmp" + elem)

fps = args.fps
MAX_BATCH_SIZE = 10
global semaphore
semaphore = False
# Start and clean Redis server
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushdb()


def number_key(name):
    parts = re.findall('[^0-9]+|[0-9]+', name)
    L = []
    for part in parts:
        try:
            L.append(int(part))
        except ValueError:
            L.append(part)
    return L


def clear_tmp_images():
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    for elem in os.listdir("tmp/"):
        if elem:
            os.remove("tmp/" + elem)


if args.inception:
    inception_model_obj = InceptionModel(base_dir)


def classify_batch(batch):
    if args.inception:
        if len(batch) != 0:
            res = inception_model_obj.inception_scores(batch)
    else:
        if len(batch) != 0:
            res = dragon_model.run_score(batch)

    return res


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/', methods=['POST'])
@app.route('/api/v1/processVideo', methods=['POST'])
def handle_url():
    global semaphore
    semaphore = False
    r.flushdb()
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
    print("Executing ffmpeg")
    classification_thread = Thread(target=start_classification, args=())
    classification_thread.start()
    ffmpeg_thread = Thread(target=get_frames(video_name, args.fps), args=())
    ffmpeg_thread.start()
    return Response(json.dumps(app.config['video']), mimetype="application/json")
    # return render_template('index.html', config=app.config)


def start_classification():
    print("-------- Starting classification --------")
    listdir = os.listdir("tmp")
    print("Listed tmp, size", len(listdir))
    date_n_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    with open("tmp-output/classifier" + date_n_time + ".csv", 'w') as csvfile:
        scorewriter = csv.writer(csvfile, delimiter=';',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        j = 0
        while not semaphore or len(sorted(os.listdir("tmp"), key=number_key)) > 0:
            data = sorted(os.listdir("tmp"), key=number_key)
            batch = get_batch(data)
            if len(batch):
                res = classify_batch(batch)
                for i in range(len(res)):
                    time_stamp = (j + i) / float(fps)
                    if not r.set(j + i, json.dumps({'time': "{0:.4f}".format(time_stamp), 'score': str(res[i])})):
                        print("An error occurred and the dictionary could not be saved")
                    if args.test:
                        scorewriter.writerow([time_stamp, batch[i], res[i]])
                j += i + 1
                if args.test:
                    dest = ['tmp-output/' + im[4:] for im in batch]
                    list(map(copyfile, batch, dest))
                list(map(os.remove, batch))
    if not args.test:
        os.remove("tmp-output/classifier" + date_n_time + ".csv")
    global semaphore
    semaphore = False
    print("All images classified")


@app.route("/api/v1/returnClassification", methods=['POST'])
def return_classification():
    response = {}
    scores = []
    for key in r.keys():
        scores.append(json.loads(r.get(key).decode("utf-8")))
        r.delete(key)
    response['scores'] = scores
    response['classification'] = semaphore
    return Response(json.dumps(response).replace("\'", "\""), mimetype="application/json")


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


@app.route('/static/videos/<path:path>')
def send_video(path):
    return send_from_directory('static/video', path)


def get_batch(data):
    if len(data) > MAX_BATCH_SIZE:
        return ['tmp/' + img for img in data[0:MAX_BATCH_SIZE]]
    else:
        return ['tmp/' + img for img in data]


def download_video(video_url, ydl_opts):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])


def get_frames(video_name, fps):
    os.system("ffmpeg -i static/video/" + video_name + ".mp4 -vf fps=" + fps + " -q:v 1 " + "tmp/%06d.jpg")
    global semaphore
    semaphore = True


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6006, threaded=True)
