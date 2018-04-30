import os
import tensorflow as tf
import common.cnn as cnn
import common.dataset as dataset
import json

real_path = os.path.realpath(__file__)
base_dir = real_path[:real_path.rfind("/")]
n_classes = 1
config = json.load(open("config.json"))
sizeX = config["width"]
sizeY = config["height"]
sizeZ = config["depth"]
n_classes = config["n_classes"]


class DragonModel(object):

    def __init__(self,
                 input_shape, get_conv_net, n_classes):
        """
        Model with evaluator function
        :param input_shape: desired shape of images
        :param get_conv_net: function that returns the evaluation of the input images
        :param get_variables: function that return weights and biases
        :param n_classes: number of classes to classify
        """
        threshold = config["threshold"]

        self.input_shape = input_shape
        n_input = input_shape[0]*input_shape[1]*input_shape[2]    # Images data input (img shape: h*v*deep)
        # tf Graph input
        keep_prob = tf.constant(1., dtype=tf.float32)  # dropout (keep probability)
        apply_dropout = tf.constant(False, dtype=tf.bool)
        conv_regularization = tf.constant(0., dtype=tf.float32)
        self.x = tf.placeholder(tf.float32, [None, n_input], name="x")
        # weights, biases = get_variables(input_shape, n_classes)
        self.logits, _ = get_conv_net(input_shape[0], input_shape[1], self.x, n_classes, keep_prob, apply_dropout, conv_regularization)
        self.score = tf.sigmoid(self.logits)
        if n_classes == 1:
            self.evaluator = tf.greater(self.score, threshold)
        else:
            self.score = tf.nn.softmax(self.logits)
            self.evaluator = tf.argmax(self.logits, 1)
            self.top_pred = tf.nn.top_k(self.evaluator, 3)

        # Initializing the variables
        init = tf.global_variables_initializer()
        model_path = base_dir + "/saves/320_reg_06_rate_006_2fc.ckpt-18432"
        saver = tf.train.Saver()
        self.tf_session = tf.Session()
        self.tf_session.run(init)
        saver.restore(self.tf_session, model_path)

    def run_evaluator(self, image_paths):
        results, logits = self.tf_session.run([self.evaluator, self.logits],
                                              {self.x: (list(map(self._load_image_from_path, image_paths)))})
        return logits.flatten()

    def run_score(self, image_paths):
        return self.tf_session.run(self.score, {
            self.x: (list(map(self._load_image_from_path, image_paths)))
        }).flatten()

    def _load_image_from_path(self, image_path):
        return dataset.load_image(image_path, (self.input_shape[0], self.input_shape[1]))


dragon_model = DragonModel([sizeX, sizeY, sizeZ], cnn.conv_net_shallow_222222_2, n_classes)
