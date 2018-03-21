#coding:utf-8
import urllib2

#返回的是响应类文件对象，并不是可读的文本内容
response=urllib2.urlopen('http://www.baidu.com')

#要想读取内容，使用类对象的read()方法
html=response.read()

print html