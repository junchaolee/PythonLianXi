#coding:utf-8
"""
代理设置ProxyHandler
urlopen()不能使用代理，必须使用自定义的opner
"""
import urllib2
#构造两个HTTPHandler，一个有IP代理，一个没有
httpproxy_handler=urllib2.ProxyHandler({"http":"61.147.118.26:35270"})
nullproxy_handler=urllib2.ProxyHandler({})#空的也要传一个字典对象

#定义代理开关
proxySwitch=True

if proxySwitch:
    opener=urllib2.build_opener(httpproxy_handler)
else:
    opener=urllib2.build_opener(nullproxy_handler)

request=urllib2.Request("http://www.baidu.com")

response=opener.open(request)

print response.read()


