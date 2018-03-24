#coding:utf-8
import urllib2
authproxy_handler=urllib2.ProxyHandler({"http":"username:password@61.147.118.26:80"})
opener=urllib2.build_opener(authproxy_handler)
request=urllib2.Request("http://www.baidu.com")
response=opener.open(request)
print response.read()
