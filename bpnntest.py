import tensorflow as tf
import numpy as np
import json
import os
from urllib.request import urlopen
import matplotlib.pyplot as plt

size = 240  #calculate length
node = 360 #middle nodes count
plength = 48 #predict length
delta = 1;
precision = 1
loop = 0
batchCount = 48

W1 = tf.Variable(tf.random_uniform([size*4,node],-1.0,1.0,dtype=tf.double), dtype=tf.double)
b1 = tf.Variable(tf.zeros([node],dtype=tf.double), dtype=tf.double)
W2 = tf.Variable(tf.random_uniform([node,1],-1.0,1.0,dtype=tf.double), dtype=tf.double)
b2 = tf.Variable(tf.zeros([1],dtype=tf.double), dtype=tf.double)

x = tf.placeholder(tf.double, shape=[None, size*4])
y_ = tf.placeholder(tf.double, shape=[None, 1])

sess = tf.InteractiveSession()

def cutArray(arr,first=0,size=1200):
    last = first + size
    calsize = last + plength
    calarray = arr[last:calsize,]
    array1 = arr[first:last,]
    array1.shape = (size*4)
    return (array1,calarray[0,2], calarray.min(0)[2],calarray.max(0)[2])

def nextBatch(arr,count):
    global loop
    len = arr.shape[0]
    batch1 = np.zeros(shape=[count, size * 4], dtype=np.double)
    batch2 = np.zeros(shape=[count, 1], dtype=np.double)

    if loop + count > len-size-plength:
        loop = (loop + count) % (len-size-plength)

    for i in range(loop,loop+count):
        (array1,current,min,max) = cutArray(arr,i,size)
        batch1[i-loop] = array1
        rate = (current - min) / (max - min)
        batch2[i-loop] = rate
    loop += count
    return (batch1,batch2)

'''
def predictArray(arr):
    pl = arr.shape[0]
    for i in range(0, pl - size):
        array1 = arr[i:i + size]
        array1.shape = (size * 4)
        predict[i] = array1
    return predict
'''
def predictArray(arr,count):
    pl = arr.shape[0]
    for i in range(pl - size - count, pl - size):
        array1 = arr[i:i + size]
        array1.shape = (size * 4)
        predict[i - pl + size + count] = array1

    return predict

def getData(y):
    if y:
        urlGetData = 'https://ichess.sinaapp.com/other/bpnn.php?y=1'
    else:
        urlGetData = 'https://ichess.sinaapp.com/other/bpnn.php'
    for line in urlopen(urlGetData):
        line = line.decode('utf-8')
        # file = open('data.json')
        # line = file.readline()
        arrLoad = json.loads(line)
        arrResult = np.array(arrLoad, dtype=np.double)
        return arrResult

arr = getData(True)
arrPredict = getData(False)
pl = arrPredict.shape[0]

predict = np.zeros(shape=[batchCount, size * 4],dtype = np.double)

result1 = tf.nn.tanh(tf.matmul(x,W1) + b1)
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
path = 'saver%d-%d/' % (size,node)

# 判断模型保存路径是否存在，不存在就创建
if not os.path.exists(path):
    os.mkdir(path)

init = tf.global_variables_initializer()
sess.run(init)

if os.path.exists('%scheckpoint' % path): #判断模型是否存在
    saver.restore(sess, '%smodel.ckpt' % path) #存在就从模型中恢复变量

for step in range(0,200000001):
    (batch1, batch2) = nextBatch(arr,batchCount)
    train_step.run(feed_dict={x: batch1, y_: batch2})

    if step % 20 == 0:
        save_path = saver.save(sess, '%smodel.ckpt' % path)
        delta = sess.run(cross_entropy, feed_dict={x: batch1,
                                           y_: batch2});
        print(step, delta, precision)  # , sess.run(y1,feed_dict={x: batch1, y_: batch2}), batch2

        if delta < 0.01:
            predict = predictArray(arrPredict, batchCount)
            result = sess.run(y_conv, feed_dict={x: predict});
            plt.plot(range(batchCount), result, 'g', label='broadcast')

            plt.plot(range(batchCount), sess.run(y_conv, feed_dict={x: batch1, y_: batch2}), 'p', label='predict')
            plt.plot(range(batchCount), sess.run(y_, feed_dict={x: batch1, y_: batch2}), 'r', label='broadcast')
            plt.grid()
            plt.show()
            plt.close()
            break





