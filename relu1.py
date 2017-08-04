import tensorflow as tf

w = tf.Variable([[1.0,2.0,-0.5],[-0.9,0.1,11.2]])
#w_nn = tf.nn.relu(w)
w_nn = tf.nn.tanh(w)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
print(sess.run(w_nn))
sess.close