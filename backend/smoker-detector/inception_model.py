import tensorflow as tf


class InceptionModel(object):

    def __init__(self, base_dir):
        self.sess = tf.Session()
        label_lines = [line.rstrip() for line
                           in tf.gfile.GFile(base_dir + "/retrained_labels.txt")]

        with tf.gfile.FastGFile(base_dir + "/retrained_graph.pb", 'rb') as f:
        # with tf.gfile.FastGFile(base_dir + "/test_retrain_aug.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            _ = tf.import_graph_def(graph_def, name='')

        self.softmax_tensor = self.sess.graph.get_tensor_by_name('final_result:0')

    def inception_score(self, image_path):
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        # Feed the image_data as input to the graph and get first prediction
        predictions = self.sess.run(self.softmax_tensor, {'DecodeJpeg/contents:0': image_data})
        return predictions[0][1]  # this is where the smokers score is saved in inception
        # return predictions[0][0]  # this is where the smokers score is saved in inception retrained

    def inception_scores(self, image_paths):
        score = []
        for image in image_paths:
            score.append(self.inception_score(image))
        return score
