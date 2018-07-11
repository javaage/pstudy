import tushare as ts
import numpy as np
import smail
import codedata
import json
import time
import pandas

highcodes = [];
lowcodes = [];
count = 0
hightotal = 0
lowtotal = 0
# pe41 = ['600004','600000']

basics = pandas.read_json('df.json',orient='table')
print(basics)
# print(basics[basics['pe'] < 41])
#basics = basics[basics['pe'] < 41][basics['pe'] > 0][basics['pb'] < 5][basics['pb'] > 0][basics['rev'] > 0][basics['profit'] > 0][basics['industry'] != '区域地产'][basics['industry'] != '全国地产'][basics['industry'] != '银行']
#pe41 = basics.index
# print(basics.index)
# # basics.to_json('/home/ubuntu/workspace/pstudy/prod/basics.json',orient='records')
