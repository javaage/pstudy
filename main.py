#-*- coding:utf-8 –*-
from flask import Flask
from flask import request
import tushare as ts
import time
import datetime
import json

app=Flask(__name__)
@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
@app.route('/user/<name>')
def user(name):
  now = datetime.datetime.now()
  delta = datetime.timedelta(days=-90)
  n_days = now + delta
  day90 = n_days.strftime('%Y-%m-%d')

  basics = ts.get_stock_basics()
  basics = basics[basics['pe'] < 41]
  basics = basics[basics['pe'] > 0]
  basics = basics[basics['pb'] < 5]
  basics = basics[basics['pb'] > 0]
  basics = basics[basics['rev'] > 0]
  basics = basics[basics['profit'] > 0]
  basics = basics[basics['industry'] != '区域地产']
  basics = basics[basics['industry'] != '全国地产']
  basics = basics[basics['industry'] != '银行']

  codes = [];
  pe41 = basics.index
  # common.allcode
  for code in pe41:
    df = ts.get_k_data(code, start='1990-12-01')
    # print df.tail(60)['close'].max()/df.tail(60)['close'].min()
    if (df.shape[0] > 0 and df.tail(60)['close'].max() / df.tail(60)['close'].min() < 1.3):
      if (df[df['close'] > df.iat[df.shape[0] - 1, 2]]['date'].max() < day90):
        codes.append(code)

  #print(codes)

  return ','.join(codes)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5050)

"""    
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

class MainHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        self.set_header('content-type', 'text/plain')
        self.write('Hello, World! ')

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(5050)
    tornado.ioloop.IOLoop.current().start()
"""
