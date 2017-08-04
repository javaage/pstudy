import tensorflow as tf
import numpy as np

#x_data = np.float32([[1.0, 2.0, 5.0, 3.0, 4.0, 7.0, 6.0], [1.0, 3.0, 4.0, 2.0, 3.0, 9.0, 8.0]])
x_data = np.float32(np.random.rand(2,100))
print(x_data)

#y_data = [9.0, 16.0, 27.0, 13.0, 16.0, 39.0, 34.0]
y_data = np.dot([2, 3], x_data) + 4
print(y_data)

print(tf.ones([1])*4)
#print([4])

b = tf.Variable(tf.ones([1])*4)
W = tf.Variable(tf.random_uniform([1,2], 1, 4))
#b = tf.Variable([4])
#W = tf.Variable([3, 2])

y = tf.matmul(W,x_data) + b

square = tf.square(y - y_data)

loss = tf.reduce_mean(square)

optimizer = tf.train.GradientDescentOptimizer(0.4)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(0,201):
    sess.run(train)
    if i % 20 == 0:
        print(i, sess.run(W), sess.run(b), sess.run(square))



