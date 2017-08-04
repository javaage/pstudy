import tensorflow as tf
import numpy as np
import jsontest
import os
from urllib.request import urlopen

size = 240 * 5
count = 500
W1 = tf.Variable(tf.random_uniform([size*4,size],-1.0,1.0), dtype=tf.float32)
b1 = tf.Variable(tf.zeros([count, size]), dtype=tf.float32)
W2 = tf.Variable(tf.random_uniform([size,1],-1.0,1.0), dtype=tf.float32)
b2 = tf.Variable(tf.zeros([1]), dtype=tf.float32)

x = tf.placeholder(tf.float32, shape=[None, size*4])
y_ = tf.placeholder(tf.float32, shape=[None, 1])

batch1 = np.zeros(shape=[count, size * 4],dtype = np.float32)
batch2 = np.zeros(shape=[count, 1],dtype = np.float32)

sess = tf.InteractiveSession()

def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

x_image = tf.reshape(x, [-1,28,28,1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
sess.run(tf.initialize_all_variables())

def cutArray(arr,first=0,size=1200):
    last = first + size
    calsize = last + 240/5
    calarray = arr[last:calsize,]
    array1 = arr[first:last,]
    array1.shape = (size*4)
    return (array1,calarray[0,2], calarray.min(0)[2],calarray.max(0)[2])

def getData(arr):
    len = arr.shape[0]
    for i in range(count):
        (array1,current,min,max) = cutArray(arr,i,size)
        batch1[i] = array1
        rate = (current - min) / (max - min)
        batch2[i] = rate
    return (batch1,batch2)

file = open('data.json')
line = file.readline()
arr = jsontest.loads(line)
arr = np.array(arr, dtype=np.float32)
(batch1,batch2) = getData(arr)

for i in range(200):
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict={
        x:batch1, y_: batch2, keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(feed_dict={x: batch1, y_: batch2, keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={x: batch1, y_: batch2, keep_prob: 1.0}))