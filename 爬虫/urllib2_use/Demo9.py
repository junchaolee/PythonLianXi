#coding:utf-8
"""
处理HTTPS请求 SSL证书验证
SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:661)
"""
import urllib2
import ssl#导入Python的ssl模块，让程序忽略验证

#忽略未经证实的SSL证书认证
context=ssl._create_unverified_context()

url="https://www.12306.cn/mormhweb/"

ua_header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

request=urllib2.Request(url,headers=ua_header)

#urlopen()方法中指明添加context参数
response=urllib2.urlopen(request,context=context)

print response.read()