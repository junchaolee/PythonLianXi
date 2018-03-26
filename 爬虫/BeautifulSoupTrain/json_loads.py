#encoding:utf-8
"""
json模块提供了四个功能：dumps、dump、loads、load，用于字符串 和 python数据类型间进行转换。
"""
import chardet
import json
strList='[1,2,3,4,4]'
strDict='{"city":"杭州","name":"胖胖"}'

#loads()实现Json格式字符串解码转换成Python对象
print json.loads(strList)
print json.loads(strDict)# json数据自动按Unicode存储

print '*'*60

#dumps()实现Python类型转换为json字符串
listStr=[4,5,6,7,2,3]
tupleStr=(2,23,54,2,6,8)
dictStr={"city":"北京","name":"熊猫"}

print json.dumps(listStr)
print json.dumps(tupleStr)
"""
注意：json.dumps() 序列化时默认使用的ascii编码
 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
 chardet.detect()返回字典, 其中confidence是检测精确度
 chardet是一个非常优秀的编码识别模块，可通过pip安装
"""
print chardet.detect(json.dumps(dictStr))
print json.dumps(dictStr,ensure_ascii=False)
print chardet.detect(json.dumps(dictStr,ensure_ascii=False))