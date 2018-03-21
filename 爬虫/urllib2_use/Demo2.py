#coding:utf-8
'''
要想执行更复杂的操作，必须创建一个Reqest实例来作为
urlopen()的参数，而请求的地址作为reqeust实例的参数
'''
import urllib2

#构造一个request实例
url="http://www.baidu.com"
ua_header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
request=urllib2.Request(url,headers=ua_header)
#返回的是响应类文件对象，并不是可读的文本内容
response=urllib2.urlopen(request)
#要想读取内容，使用类对象的read()方法
html=response.read()

print html