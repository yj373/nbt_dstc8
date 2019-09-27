import tensorflow as tf
tf.reset_default_graph()

a = tf.constant(2, name='a')
b = tf.constant(3, name='b')
c = tf.add(a, b, name='addition')

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    print(sess.run(c))