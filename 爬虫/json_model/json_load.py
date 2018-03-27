#coding:utf-8
"""读取文件中Json形式的字符串元素，转化成python类型"""
import json

strList=json.load(open('listStr.json'))
print strList

strDict=json.load(open('dictStr.json'))
print strDict