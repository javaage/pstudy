from flask import Flask
from flask import request
import tushare as ts
import time
import datetime
import json

import numpy as np

now = datetime.datetime.now()
delta = datetime.timedelta(days=-90)
n_days = now + delta
day90 = n_days.strftime('%Y-%m-%d')

basics = ts.get_stock_basics()

print(ts.get_k_data('399300', index=True,start='2016-10-01', end='2016-10-31'))

# basics = basics[basics['pe'] < 41]
# basics = basics[basics['pe'] > 0]
# basics = basics[basics['pb'] < 5]
# basics = basics[basics['pb'] > 0]
# basics = basics[basics['rev'] > 0]
# basics = basics[basics['profit'] > 0]
# basics = basics[basics['industry'] != '区域地产']
# basics = basics[basics['industry'] != '全国地产']
# basics = basics[basics['industry'] != '银行']
#
codes = [];
# pe41 = basics.index
# print('begin')
# # common.allcode

pe41 = []

for code in pe41:
  df = ts.get_k_data(code, start='1990-12-01')
  # print df.tail(60)['close'].max()/df.tail(60)['close'].min()
  if (df.shape[0] > 0 and df.tail(60)['close'].max() / df.tail(60)['close'].min() < 1.3):
    if (df[df['close'] > df.iat[df.shape[0] - 1, 2]]['date'].max() < day90):
      codes.append(code)
#
# print(codes)

# filter=df['close']<=df.loc[df.shape[0]-1,'close']
# filter[filter[filter==False][-1:].index[0]+1:].shape[0]

# minvalue=filter[filter==False][-1:].index[0]+1
# minvalue=filter[filter==False][-1:]
# filter[minvalue.index[0]+1:].shape[0]

