import tensorflow as tf
import numpy as np
import jsontest
import os
from urllib.request import urlopen

size = 240  #
count = 100 #template size
W1 = tf.Variable(tf.random_uniform([size*4,size],-1.0,1.0,dtype=tf.double), dtype=tf.double)
b1 = tf.Variable(tf.zeros([count, size],dtype=tf.double), dtype=tf.double)
W2 = tf.Variable(tf.random_uniform([size,1],-1.0,1.0,dtype=tf.double), dtype=tf.double)
b2 = tf.Variable(tf.zeros([1],dtype=tf.double), dtype=tf.double)

x = tf.placeholder(tf.double, shape=[None, size*4])
y_ = tf.placeholder(tf.double, shape=[None, 1])

batch1 = np.zeros(shape=[count, size * 4],dtype = np.double)
batch2 = np.zeros(shape=[count, 1],dtype = np.double)

sess = tf.InteractiveSession()

def cutArray(arr,first=0,size=1200):
    last = first + size
    calsize = last + 48
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


for line in urlopen('http://ichess.sinaapp.com/other/bpnn.php'):
    line = line.decode('utf-8')
#file = open('data.json')
#line = file.readline()
arr = jsontest.loads(line)
arr = np.array(arr,dtype=np.double)

(batch1,batch2) = getData(arr)

result1 = tf.nn.tanh(tf.matmul(x,W1) + b1)
print(result1.shape)
print(W2.shape)
y_conv = tf.nn.sigmoid(tf.matmul(result1,W2) + b2)

#cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
cross_entropy = tf.reduce_sum(tf.square(y_ - y_conv))
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)
#train_step = tf.train.GradientDescentOptimizer(1e-4).minimize(cross_entropy)
#loss = tf.reduce_mean(tf.square(y1-y_))
#optimizer = tf.train.GradientDescentOptimizer(0.01)
#train_step = optimizer.minimize(loss)

# 模型保存加载工具
#saver = tf.train.Saver()
saver=tf.train.Saver([W1,b1,W2,b2])
path = 'saver%d-%d/' % (size,count)

# 判断模型保存路径是否存在，不存在就创建
if not os.path.exists(path):
    os.mkdir(path)

init = tf.global_variables_initializer()
sess.run(init)

if os.path.exists('%scheckpoint' % path): #判断模型是否存在
    saver.restore(sess, '%smodel.ckpt' % path) #存在就从模型中恢复变量
    print('W2', sess.run(W2))



for step in range(0,200000001):
    #sess.run(train_step,feed_dict={x: batch1, y_: batch2})
    train_step.run(feed_dict={x: batch1, y_: batch2})
    if step % 20 == 0:
        save_path = saver.save(sess, '%smodel.ckpt' % path)
        print(step, sess.run(y_, feed_dict={x: batch1, y_: batch2}))
        print('Predict')
        print(step, sess.run(y_conv, feed_dict={x: batch1, y_: batch2}))
        #print(batch2[0:15, 0])

        print('W2', sess.run(W2))
        print('b2', sess.run(b2))

        delta = sess.run(cross_entropy, feed_dict={x: batch1,
                                           y_: batch2});
        print(step, delta)  # , sess.run(y1,feed_dict={x: batch1, y_: batch2}), batch2

        if delta < 10e-10:
            break





