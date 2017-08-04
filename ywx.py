import tensorflow as tf
import numpy as np

sess = tf.Session()

#x_data = tf.random_uniform((20,1),1,100)
#print(sess.run(x_data))

#y_data = x_data * 2 + tf.random_uniform((20,1),0,0.2)
#print(sess.run(y_data))

x_data = np.float32(np.random.rand(3,100))
print(x_data)

#y_data = [9.0, 16.0, 27.0, 13.0, 16.0, 39.0, 34.0]
y_data = np.dot([3,4,5], x_data) + 5 + np.random.random((3,100))
print(y_data)

W = tf.Variable(tf.random_uniform((1,3),0,1))
#b = tf.Variable(tf.random_uniform((1),0.5,0.5))
b = tf.Variable(tf.ones([1])*4)

y = tf.matmul(W, x_data) + b
square = tf.square(y - y_data)

loss = tf.reduce_mean(square)

optimizer = tf.train.GradientDescentOptimizer(0.4)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess.run(init)

for i in range(1,201):
    sess.run(train)
    if i % 20 == 0:
        print(i, sess.run(W),sess.run(b),sess.run(loss))
