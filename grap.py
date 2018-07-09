import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

m = tf.get_variable("m",[],initializer=tf.constant_initializer(0.))
b = tf.get_variable("b",[],initializer=tf.constant_initializer(0.))

init = tf.global_variables_initializer()

y_guess = m * x * x + b
loss = tf.square(y-y_guess)
optimizer = tf.train.GradientDescentOptimizer(1e-3)
train_op = optimizer.minimize(loss)
#sess = tf.Session()
sess = tf.InteractiveSession()
sess.run(init)

for step in range(0,20000):
  train_op.run(feed_dict={x: [1,2,3], y: [3,6,11]})

print(sess.run(m))
print(sess.run(b))
#print(sess.run(loss))
result = sess.run(loss,feed_dict={x: [1,2,3],  y: [2,3,4]})
print(result)

# print("graph")
#
# count_variable = tf.get_variable("count",[])
# zero_node = tf.constant(0.)
# assgin_node = tf.assign(count_variable,zero_node)
# sess = tf.Session()
# sess.run(assgin_node)
# print(sess.run(count_variable))


