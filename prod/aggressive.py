import tushare as ts
import numpy as np
import smail
import codedata
import json
import time

highcodes = [];
lowcodes = [];
count = 0
hightotal = 0
lowtotal = 0
# pe41 = ['600004','600000']
for code in codedata.pe41:
  df = ts.get_k_data(code, start='1990-12-01')
  if df.shape[0]>30:
    count += 1
    highfilter= df['close'] <= df.loc[df.shape[0] - 1, 'close']
    high = highfilter[highfilter[highfilter == False][-1:].index[0] + 1:-1].shape[0]
    hightotal += high
    highcodes.append([high, code])

    lowfilter = df['close'] >= df.loc[df.shape[0] - 1, 'close']
    low = lowfilter[lowfilter[lowfilter == False][-1:].index[0] + 1:-1].shape[0]
    lowtotal += low
    lowcodes.append([low, code])
    print(code)

highcodes.sort(reverse=True)
subject = "High:%f, Low:%f, Date: %s" % (round(hightotal / count, 2), round(lowtotal / count, 2), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
content = "High:%s, Low:%s" % (json.dumps(highcodes),json.dumps(lowcodes))
smail.sendMail(subject,content)
