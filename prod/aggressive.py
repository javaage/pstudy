import tushare as ts
import numpy as np
import smail
import json
import time
import pandas
import logging
import pymysql
import datetime

highcodes = [];
lowcodes = [];
count = 0
hightotal = 0
lowtotal = 0
# pe41 = ['600004','600000']

logging.basicConfig(filename='log.txt',level=logging.DEBUG)

basics = pandas.read_json('df.json',orient='table')
basics = basics[basics['pe'] < 41][basics['pe'] > 0][basics['pb'] < 5][basics['pb'] > 0][basics['rev'] > 0][basics['profit'] > 0][basics['industry'] != '区域地产'][basics['industry'] != '全国地产'][basics['industry'] != '银行']
pe41 = basics.index
print(basics.index)

now = datetime.datetime.now().strftime('%Y-%m-%d')
# conn = pymysql.connect('localhost', 'root', 'a123456', 'tushare')
conn = pymysql.connect('pactera.cifdw7epxuja.ap-northeast-2.rds.amazonaws.com', 'pactera', '19786028', 'test')

cursor = conn.cursor()
sql = "SELECT AGGR_CODE FROM TSHR_AGGR WHERE AGGR_DATE='%s'" % now
cursor.execute(sql);
results = cursor.fetchall()

for code in pe41:
  code = "%06d" % code
  logging.debug(code)

  if(code in results):
    break;

  df = ts.get_k_data(code, start='1990-12-01')
  if df.shape[0]>30:
    count += 1
    highfilter = df['close'] <= df.loc[df.shape[0] - 1, 'close']
    if (highfilter[highfilter == False].shape[0] > 0):
      high = highfilter[highfilter[highfilter == False][-1:].index[0] + 1:-1].shape[0]
      hightotal += high
    else:
      high = highfilter.shape[0]
      hightotal += high
    highcodes.append([high, code])

    lowfilter = df['close'] >= df.loc[df.shape[0] - 1, 'close']
    if (lowfilter[lowfilter == False].shape[0] > 0):
      low = lowfilter[lowfilter[lowfilter == False][-1:].index[0] + 1:-1].shape[0]
      lowtotal += low
    else:
      low = lowfilter.shape[0]
      lowtotal += low
    lowcodes.append([low, code])
    cursor = conn.cursor()
    sql = 'INSERT INTO TSHR_AGGR (`AGGR_DATE`,`AGGR_CODE`,`AGGR_HIGH`,`AGGR_LOW`) VALUES (%s,%s,%s,%s);'
    cursor.execute(sql, (now, code, high, low));
    conn.commit()
    # logging.debug(highcodes)
    # logging.debug(lowcodes)

conn.close();
highcodes.sort(reverse=True)
lowcodes.sort(reverse=True)
subject = "High:%f, Low:%f, Date: %s" % (round(hightotal / count, 2), round(lowtotal / count, 2), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
content = "High:%s, \r\n Low:%s" % (json.dumps(highcodes),json.dumps(lowcodes))
smail.sendMail(subject,content)
