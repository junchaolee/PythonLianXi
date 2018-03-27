#coding:utf-8
"""
JsonPath 是一种信息抽取类库，是从JSON文档中抽取指定信息的工具，提供多种语言实现版本，
包括：Javascript, Python， PHP 和 Java
JsonPath 对于 JSON 来说，相当于 XPATH 对于 XML
XPath 	JSONPath 	描述
/ 	    $ 	    根节点
.   	@ 	    现行节点
/ 	    .or[] 	取子节点
..  	n/a 	取父节点，Jsonpath未支持
//  	..  	就是不管位置，选择所有符合条件的条件
* 	    * 	    匹配所有元素节点
@   	n/a 	根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要。
[]  	[] 	    迭代器标示（可以在里边做简单的迭代操作，如数组下标，根据内容选值等）
|   	[,] 	支持迭代器中做多选。
[]  	?() 	支持过滤操作.
n/a 	()  	支持表达式计算
()  	n/a 	分组，JsonPath不支持
"""
import json
import urllib2
import jsonpath
import chardet

url='http://www.lagou.com/lbs/getAllCitySearchLabels.json '
request=urllib2.Request(url)
response=urllib2.urlopen(request)
html=response.read()
# print html
# json.dump(html,open('lagou.json','w'),ensure_ascii=False)

#将json格式的字符串转换成python对象
json_obj=json.loads(html)

#从根节点，匹配name节点
citylist=jsonpath.jsonpath(json_obj,'$..name')
print type(citylist)
# print citylist
fp=open('city.json','w')
content=json.dumps(citylist,ensure_ascii=False)
print content
fp.write(content.encode('utf-8'))
fp.close()


