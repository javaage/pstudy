import tushare as ts
import numpy as np
import smail
import codedata
import json
import time
from pandas import *

# df = ts.get_stock_basics()
# df.to_json('df.json',orient='table')
# DataFrame.to_json()
#
# # basics.to_json('/home/ubuntu/workspace/pstudy/prod/basics.json',orient='records')
#
basics = pandas.read_json('df.json',orient='table')
basics = basics[basics['pe'] < 41][basics['pe'] > 0][basics['pb'] < 5][basics['pb'] > 0][basics['rev'] > 0][basics['profit'] > 0][basics['industry'] != '区域地产'][basics['industry'] != '全国地产'][basics['industry'] != '银行']
print(basics.index)

# df = pandas.read_json('d:/workspace/pstudy/prod/df.json',orient='records');
# print(df.type)
