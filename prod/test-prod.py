import pymysql
import datetime
import tushare as ts

df = ts.get_k_data('600000', start='2018-07-01')
print(df)
