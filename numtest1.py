import tensorflow as tf
import numpy as np

x_data = np.float32(np.random.rand(2,100))
#print(x_data)

y_data = np.dot([0.100, 0.200], x_data) + 0.300
#print(y_data)

#print(tf.zeros([1,2,4]))
b = tf.Variable(tf.zeros([1]))
#print(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1,2],-1.0,1.0))
#print(tf.random_uniform([1,2],-1.0,1.0))
y = tf.matmul(W, x_data) + b

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(loss)
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
for step in range(0,21):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(W), sess.run(b), sess.run(tf.square(y-y_data)))



