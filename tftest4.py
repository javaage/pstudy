import tensorflow as tf

with tf.Session() as sess:
    with tf.device("Cpu:0"):
        matrix1 = tf.Variable([[3.,3.],[2.,2.]])
        matrix2 = tf.constant([[2.],[2.]])

        #matrix3 = tf.matmul(matrix1.initializer.run(),matrix2)

        #print(matrix1.initializer.run())
        print(matrix2)
        #print(sess.run(matrix3))