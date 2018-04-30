import tensorflow as tf
num_of_images_to_show = 10  # this is the number of images to be shown in the summary of intermediate layers


def conv_net_shallow_22222(image_x, image_y, x, n_classes, keep_prob, apply_dropout, conv_regularization):
    x = tf.reshape(x, shape=[-1, image_y, image_x, 3])
    conv_regularizer = tf.contrib.layers.l2_regularizer(scale=conv_regularization)
    kernel = [5, 5]
    pool_size = [2, 2]
    stride = 2
    first_layer_features = 16
    second_layer_features = 16
    third_layer_features = 16
    fourth_layer_features = 32
    fc_layer_features = 128
    deviation = 0.15
    tf.summary.image("input", x, max_outputs=num_of_images_to_show, collections=['image'])

    conv_1 = conv_2d_layer(x, 'conv1', first_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    conv_2 = conv_2d_layer(conv_1, 'conv2', second_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_1 = tf.layers.max_pooling2d(inputs=conv_2, pool_size=pool_size, strides=stride)

    conv_3 = conv_2d_layer(pool_1, 'conv3', third_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_2 = tf.layers.max_pooling2d(inputs=conv_3, pool_size=pool_size, strides=stride)

    conv_4 = conv_2d_layer(pool_2, 'conv4', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_3 = tf.layers.max_pooling2d(inputs=conv_4, pool_size=pool_size, strides=stride)

    conv_5 = conv_2d_layer(pool_3, 'conv5', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_4 = tf.layers.max_pooling2d(inputs=conv_5, pool_size=pool_size, strides=stride)

    conv_6 = conv_2d_layer(pool_4, 'conv6', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_5 = tf.layers.max_pooling2d(inputs=conv_6, pool_size=pool_size, strides=stride)

    conv_7 = conv_2d_layer(pool_5, 'conv7', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)

    flatten = tf.contrib.layers.flatten(conv_7)

    fc_1 = fully_connected(flatten, 'fc1', fc_layer_features, deviation)
    fc_1 = tf.contrib.layers.dropout(fc_1, keep_prob, is_training=apply_dropout)

    embeddings = fully_connected(fc_1, 'fc_2', fc_layer_features, deviation)
    fc_2 = tf.contrib.layers.dropout(embeddings, keep_prob, is_training=apply_dropout)

    logits = fully_connected(fc_2, 'out', n_classes, deviation, activation=None)

    return logits, embeddings


def conv_net_shallow_222222(image_x, image_y, x, n_classes, keep_prob, apply_dropout, conv_regularization):
    x = tf.reshape(x, shape=[-1, image_y, image_x, 3])
    conv_regularizer = tf.contrib.layers.l2_regularizer(scale=conv_regularization)
    kernel = [5, 5]
    pool_size = [2, 2]
    stride = 2
    first_layer_features = 16
    second_layer_features = 16
    third_layer_features = 16
    fourth_layer_features = 32
    last_layer_features = 64
    fc_layer_features = 128
    deviation = 0.15
    tf.summary.image("input", x, max_outputs=num_of_images_to_show, collections=['image'])

    conv_1 = conv_2d_layer(x, 'conv1', first_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    conv_2 = conv_2d_layer(conv_1, 'conv2', second_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_1 = tf.layers.max_pooling2d(inputs=conv_2, pool_size=pool_size, strides=stride)

    conv_3 = conv_2d_layer(pool_1, 'conv3', third_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_2 = tf.layers.max_pooling2d(inputs=conv_3, pool_size=pool_size, strides=stride)

    conv_4 = conv_2d_layer(pool_2, 'conv4', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_3 = tf.layers.max_pooling2d(inputs=conv_4, pool_size=pool_size, strides=stride)

    conv_5 = conv_2d_layer(pool_3, 'conv5', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_4 = tf.layers.max_pooling2d(inputs=conv_5, pool_size=pool_size, strides=stride)

    conv_6 = conv_2d_layer(pool_4, 'conv6', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_5 = tf.layers.max_pooling2d(inputs=conv_6, pool_size=pool_size, strides=stride)

    conv_7 = conv_2d_layer(pool_5, 'conv7', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_6 = tf.layers.max_pooling2d(inputs=conv_7, pool_size=pool_size, strides=stride)

    conv_8 = conv_2d_layer(pool_6, 'conv8', last_layer_features, kernel, deviation, conv_regularizer, 8, 8)

    flatten = tf.contrib.layers.flatten(conv_8)

    embeddings = fully_connected(flatten, 'fc1', fc_layer_features, deviation)

    fc_1 = tf.contrib.layers.dropout(embeddings, keep_prob, is_training=apply_dropout)

    logits = fully_connected(fc_1, 'out', n_classes, deviation, activation=None)

    return logits, embeddings


def conv_net_shallow_222222_2(image_x, image_y, x, n_classes, keep_prob, apply_dropout, conv_regularization):
    x = tf.reshape(x, shape=[-1, image_y, image_x, 3])
    conv_regularizer = tf.contrib.layers.l2_regularizer(scale=conv_regularization)
    kernel = [5, 5]
    pool_size = [2, 2]
    stride = 2
    first_layer_features = 16
    second_layer_features = 16
    third_layer_features = 16
    fourth_layer_features = 32
    last_layer_features = 64
    fc_layer_features = 128
    deviation = 0.15
    tf.summary.image("input", x, max_outputs=num_of_images_to_show, collections=['image'])

    conv_1 = conv_2d_layer(x, 'conv1', first_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    conv_2 = conv_2d_layer(conv_1, 'conv2', second_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_1 = tf.layers.max_pooling2d(inputs=conv_2, pool_size=pool_size, strides=stride)

    conv_3 = conv_2d_layer(pool_1, 'conv3', third_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_2 = tf.layers.max_pooling2d(inputs=conv_3, pool_size=pool_size, strides=stride)

    conv_4 = conv_2d_layer(pool_2, 'conv4', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_3 = tf.layers.max_pooling2d(inputs=conv_4, pool_size=pool_size, strides=stride)

    conv_5 = conv_2d_layer(pool_3, 'conv5', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_4 = tf.layers.max_pooling2d(inputs=conv_5, pool_size=pool_size, strides=stride)

    conv_6 = conv_2d_layer(pool_4, 'conv6', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_5 = tf.layers.max_pooling2d(inputs=conv_6, pool_size=pool_size, strides=stride)

    conv_7 = conv_2d_layer(pool_5, 'conv7', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_6 = tf.layers.max_pooling2d(inputs=conv_7, pool_size=pool_size, strides=stride)

    conv_8 = conv_2d_layer(pool_6, 'conv8', last_layer_features, kernel, deviation, conv_regularizer, 8, 8)

    flatten = tf.contrib.layers.flatten(conv_8)

    fc_1 = fully_connected(flatten, 'fc1', fc_layer_features, deviation)
    fc_1 = tf.contrib.layers.dropout(fc_1, keep_prob, is_training=apply_dropout)

    embeddings = fully_connected(fc_1, 'fc2', fc_layer_features, deviation)
    fc_2 = tf.contrib.layers.dropout(embeddings, keep_prob, is_training=apply_dropout)

    logits = fully_connected(fc_2, 'out', n_classes, deviation, activation=None)

    return logits, embeddings


def conv_net_shallow_222_2(image_x, image_y, x, n_classes, keep_prob, apply_dropout, conv_regularization):
    x = tf.reshape(x, shape=[-1, image_y, image_x, 3])
    conv_regularizer = tf.contrib.layers.l2_regularizer(scale=conv_regularization)
    kernel = [5, 5]
    pool_size = [2, 2]
    stride = 2
    first_layer_features = 16
    second_layer_features = 16
    third_layer_features = 16
    fourth_layer_features = 32
    last_layer_features = 64
    fc_layer_features = 128
    deviation = 0.15
    tf.summary.image("input", x, max_outputs=num_of_images_to_show, collections=['image'])

    conv_1 = conv_2d_layer(x, 'conv1', first_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    conv_2 = conv_2d_layer(conv_1, 'conv2', second_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_1 = tf.layers.max_pooling2d(inputs=conv_2, pool_size=pool_size, strides=stride)

    conv_3 = conv_2d_layer(pool_1, 'conv3', third_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    conv_4 = conv_2d_layer(conv_3, 'conv4', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_3 = tf.layers.max_pooling2d(inputs=conv_4, pool_size=pool_size, strides=stride)

    conv_5 = conv_2d_layer(pool_3, 'conv5', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    conv_6 = conv_2d_layer(conv_5, 'conv6', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_5 = tf.layers.max_pooling2d(inputs=conv_6, pool_size=pool_size, strides=stride)

    conv_7 = conv_2d_layer(pool_5, 'conv7', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    conv_8 = conv_2d_layer(conv_7, 'conv8', last_layer_features, kernel, deviation, conv_regularizer, 8, 8)

    flatten = tf.contrib.layers.flatten(conv_8)

    fc_1 = fully_connected(flatten, 'fc1', fc_layer_features, deviation)
    fc_1 = tf.contrib.layers.dropout(fc_1, keep_prob, is_training=apply_dropout)

    embeddings = fully_connected(fc_1, 'fc2', fc_layer_features, deviation)
    fc_2 = tf.contrib.layers.dropout(embeddings, keep_prob, is_training=apply_dropout)

    logits = fully_connected(fc_2, 'out', n_classes, deviation, activation=None)

    return logits, embeddings


def simpler_conv_net_shallow_222_2(image_x, image_y, x, n_classes, keep_prob, apply_dropout, conv_regularization):
    x = tf.reshape(x, shape=[-1, image_y, image_x, 3])
    conv_regularizer = tf.contrib.layers.l2_regularizer(scale=conv_regularization)
    kernel = [5, 5]
    pool_size = [2, 2]
    stride = 2
    first_layer_features = 16
    second_layer_features = 32
    third_layer_features = 64
    fc_layer_features = 256
    deviation = 0.15
    tf.summary.image("input", x, max_outputs=num_of_images_to_show, collections=['image'])

    conv_1 = conv_2d_layer(x, 'conv1', first_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    conv_2 = conv_2d_layer(conv_1, 'conv2', first_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_1 = tf.layers.max_pooling2d(inputs=conv_2, pool_size=pool_size, strides=stride)

    conv_3 = conv_2d_layer(pool_1, 'conv3', second_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    conv_4 = conv_2d_layer(conv_3, 'conv4', second_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_3 = tf.layers.max_pooling2d(inputs=conv_4, pool_size=pool_size, strides=stride)

    conv_5 = conv_2d_layer(pool_3, 'conv5', third_layer_features, kernel, deviation, conv_regularizer, 8, 8)
    conv_6 = conv_2d_layer(conv_5, 'conv6', third_layer_features, kernel, deviation, conv_regularizer, 8, 8)
    pool_5 = tf.layers.max_pooling2d(inputs=conv_6, pool_size=pool_size, strides=stride)

    flatten = tf.contrib.layers.flatten(pool_5)

    fc_1 = fully_connected(flatten, 'fc1', fc_layer_features, deviation)
    fc_1 = tf.contrib.layers.dropout(fc_1, keep_prob, is_training=apply_dropout)

    embeddings = fully_connected(fc_1, 'fc2', fc_layer_features, deviation)
    fc_2 = tf.contrib.layers.dropout(embeddings, keep_prob, is_training=apply_dropout)

    logits = fully_connected(fc_2, 'out', n_classes, deviation, activation=None)

    return logits, embeddings


def conv_net_shallow_2222222(image_x, image_y, x, n_classes, keep_prob, apply_dropout, conv_regularization):
    x = tf.reshape(x, shape=[-1, image_y, image_x, 3])
    conv_regularizer = tf.contrib.layers.l2_regularizer(scale=conv_regularization)
    kernel = [5, 5]
    pool_size = [2, 2]
    stride = 2
    first_layer_features = 16
    second_layer_features = 16
    third_layer_features = 16
    fourth_layer_features = 32
    fc_layer_features = 128
    deviation = 0.15
    tf.summary.image("input", x, max_outputs=num_of_images_to_show, collections=['image'])

    conv_1 = conv_2d_layer(x, 'conv1', first_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    conv_2 = conv_2d_layer(conv_1, 'conv2', second_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    pool_1 = tf.layers.max_pooling2d(inputs=conv_2, pool_size=pool_size, strides=stride)

    conv_3 = conv_2d_layer(pool_1, 'conv3', third_layer_features, kernel, deviation, conv_regularizer, 4, 4)
    conv_4 = conv_2d_layer(conv_3, 'conv4', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_2 = tf.layers.max_pooling2d(inputs=conv_4, pool_size=pool_size, strides=stride)

    conv_5 = conv_2d_layer(pool_2, 'conv5', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    conv_6 = conv_2d_layer(conv_5, 'conv6', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_3 = tf.layers.max_pooling2d(inputs=conv_6, pool_size=pool_size, strides=stride)

    conv_7 = conv_2d_layer(pool_3, 'conv7', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_4 = tf.layers.max_pooling2d(inputs=conv_7, pool_size=pool_size, strides=stride)

    conv_8 = conv_2d_layer(pool_4, 'conv8', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)
    pool_5 = tf.layers.max_pooling2d(inputs=conv_8, pool_size=pool_size, strides=stride)

    conv_9 = conv_2d_layer(pool_5, 'conv9', fourth_layer_features, kernel, deviation, conv_regularizer, 4, 8)

    flatten = tf.contrib.layers.flatten(conv_9)

    embeddings = fully_connected(flatten, 'fc1', fc_layer_features, deviation)

    fc_1 = tf.contrib.layers.dropout(embeddings, keep_prob, is_training=apply_dropout)

    logits = fully_connected(fc_1, 'out', n_classes, deviation, activation=None)

    return logits, embeddings


def conv_2d_layer(input, name, layer_features, kernel, deviation, regularizer, rows, columns):
    x_dim = input.get_shape().as_list()[1]
    y_dim = input.get_shape().as_list()[2]

    assert rows * columns == layer_features

    with tf.name_scope(name):
        conv = tf.layers.conv2d(inputs=input,
                                filters=layer_features,
                                kernel_size=kernel,
                                padding='same',
                                kernel_initializer=tf.random_normal_initializer(stddev=deviation),
                                kernel_regularizer=regularizer,
                                activation=tf.nn.relu,
                                name=name)
        conv_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, name)
        tf.summary.histogram('kernel', conv_vars[0], collections=['train'])
        tf.summary.histogram('bias', conv_vars[1], collections=['train'])

        # image_reshape(conv, x_dim, y_dim, layer_features, rows, columns, name)

    return conv


def fully_connected(input, name, layer_features, deviation, activation=tf.nn.relu):
    with tf.name_scope(name):
        fc = tf.layers.dense(input,
                             layer_features,
                             kernel_initializer=tf.random_normal_initializer(stddev=deviation),
                             activation=activation,
                             name=name)
        fc_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, name)
        tf.summary.histogram('kernel', fc_vars[0], collections=['train'])
        tf.summary.histogram('bias', fc_vars[1], collections=['train'])

        # tf.summary.image('fc', tf.transpose(tf.expand_dims(tf.expand_dims(fc, 2), 3), [0, 2, 1, 3]), max_outputs=num_of_images_to_show, collections=['image'])
    return fc


def image_reshape(image, x, y, depth, rows, columns, name, pad=4):
        for i in range(num_of_images_to_show):
            V = tf.reshape(image[i] - 1.000, (y, x, depth))
            V = tf.image.pad_to_bounding_box(V, pad, pad, y + pad, x + pad) + 1.000
            V = tf.reshape(V, (y + pad, x + pad, rows, columns))
            V = tf.transpose(V, (2, 0, 3, 1)) #cy,iy,cx,ix
            V = tf.reshape(V, (1, rows*(y + pad), columns*(x + pad), 1))
            tf.summary.image(name, V, max_outputs=1, collections=['image'])
