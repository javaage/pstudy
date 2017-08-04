import tensorflow as tf

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(4.0)

sum = tf.add(input1,input2)
mul = tf.multiply(input3,sum)

with tf.Session() as sess:
    result = sess.run([mul,sum])
    print(result)