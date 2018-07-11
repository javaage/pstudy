import tushare as ts
import numpy as np
import smail
import codedata
import json
import time
import pandas
import logging

highcodes = [];
lowcodes = [];
count = 0
hightotal = 0
lowtotal = 0
code='600009'
df = ts.get_k_data(code, start='1990-12-01')
if df.shape[0]>30:
    count += 1
    highfilter= df['close'] <= df.loc[df.shape[0] - 1, 'close']
    if(highfilter[highfilter == False].shape[0]>0):
      high = highfilter[highfilter[highfilter == False][-1:].index[0] + 1:-1].shape[0]
      hightotal += high
    else:
      high = highfilter.shape[0]
      hightotal += high
    highcodes.append([high, code])


    lowfilter = df['close'] >= df.loc[df.shape[0] - 1, 'close']
    if(lowfilter[lowfilter == False].shape[0]>0):
      low = lowfilter[lowfilter[lowfilter == False][-1:].index[0] + 1:-1].shape[0]
      lowtotal += low
    else:
      low = lowfilter.shape[0]
      lowtotal += low
    lowcodes.append([low, code])
    logging.warning(highcodes)
    logging.warning(lowcodes)
