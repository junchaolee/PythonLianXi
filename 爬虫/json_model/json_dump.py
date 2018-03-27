#coding:utf-8
#将python内置类型序列化json对象后存入文件
import json

listStr=['张三','李四']
json.dump(listStr,open("listStr.json",'w'),ensure_ascii=False)

dictStr={"姓名":"小九","年龄":45}
json.dump(dictStr,open("dictStr.json",'w'),ensure_ascii=False)