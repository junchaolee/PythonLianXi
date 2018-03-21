#coding:utf-8
'''
添加一个特定的header
'''
import urllib2

#构造一个request实例
url="http://www.slswd.com"
ua_header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
request=urllib2.Request(url,headers=ua_header)
#添加一个特定的header
request.add_header("Connection","keep-alive" )
#通过get_header()查看header信息
req_head=request.get_header(header_name="Connection")
#返回的是响应类文件对象，并不是可读的文本内容
response=urllib2.urlopen(request)
#要想读取内容，使用类对象的read()方法
html=response.read()
print req_head
print html