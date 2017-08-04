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

sess = tf.InteractiveSession()

for line in urlopen('http://ichess.sinaapp.com/other/bpnn.php'):
    line = line.decode('utf-8')

arr = jsontest.loads(line)
arr = np.array(arr,dtype=np.double)

#(batch1,batch2) = getData(arr)

result1 = tf.nn.tanh(tf.matmul(x,W1) + b1)
print(result1.shape)
print(W2.shape)
y_conv = tf.nn.sigmoid(tf.matmul(result1,W2) + b2)

# 模型保存加载工具
#saver = tf.train.Saver()
saver=tf.train.Saver([W1,b1,W2,b2])
path = 'saver%d-%d/' % (size,count)

# 判断模型保存路径是否存在，不存在就创建
if not os.path.exists(path):
    print('path not exsit')
    exit(0)

init = tf.global_variables_initializer()
sess.run(init)

if os.path.exists('%scheckpoint' % path): #判断模型是否存在
    saver.restore(sess, '%smodel.ckpt' % path) #存在就从模型中恢复变量
    print('W2', sess.run(W2))
else:
    print('model data does not exsit')
    exit(0)

for i in range(1,50):
    input = arr[-size-1:-1]
    input.shape = (size*4)
    print('result',sess.run(y_conv, feed_dict={x: [input]})[0])