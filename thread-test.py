#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
    threading._start_new_thread( print_time, ("Thread-1", 2, ))
    threading._start_new_thread( print_time, ("Thread-3", 4, ))
except:
    print("Error: unable to start thread")

while 1:
    pass
