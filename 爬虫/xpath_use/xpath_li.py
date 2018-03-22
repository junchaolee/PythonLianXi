#coding:utf-8

from lxml import etree

html=etree.parse("hello.html")
# print type(html)#<type 'lxml.etree._ElementTree'>
result=html.xpath('//li/@class')#加@class获取class属性值
print result
print type(result)
print type(result[0])