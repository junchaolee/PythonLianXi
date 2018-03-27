#encoding:utf-8
"""
json模块提供了四个功能：dumps、dump、loads、load，用于字符串 和 python数据类型间进行转换。
"""

import json
strList='[1,2,3,4,4]'
strDict='{"city":"杭州","name":"胖胖"}'

#loads()实现Json格式字符串解码转换成Python对象
print json.loads(strList)
print json.loads(strDict)# json数据自动按Unicode存储


