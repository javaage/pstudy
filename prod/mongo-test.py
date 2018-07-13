#!/usr/bin/python3

import pymongo

# myclient = pymongo.MongoClient("mongodb://52.79.236.137:27017/")
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["site2"]

mylist = [
  {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  {"_id": 2, "name": "Google", "address": "Google 搜索"},
  {"_id": 3, "name": "Facebook", "address": "脸书"},
  {"_id": 4, "name": "Taobao", "address": "淘宝"},
  {"_id": 5, "name": "Zhihu", "address": "知乎"}
]

x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
