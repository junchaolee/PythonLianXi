#coding:utf-8
"""
自定义opener
    opener是 urllib2.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。
    但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：
       1、 使用相关的 Handler处理器 来创建特定功能的处理器对象；
       2、然后通过 urllib2.build_opener()方法使用这些处理器对象，创建自定义opener对象；
       3、 使用自定义的opener对象，调用open()方法发送请求。
    如果程序里所有的请求都使用自定义的opener，可以使用urllib2.install_opener() 将自定义的 opener 对象 定义为 全局opener，
    表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）
"""
import urllib2

#step1：构造一个HTTPHandler处理器对象，支持处理http请求,HTTPHandler()添加debuglevel=1，打开Debug Log调试
http_hander=urllib2.HTTPHandler(debuglevel=1)

# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# http_handler = urllib2.HTTPSHandler()

#:step2：调用urllib2.build_opener()方法，创建支持http请求的opener()
opener=urllib2.build_opener(http_hander)

#step3:调用open()方法发送请求
request=urllib2.Request("http://www.baidu.com")
response=opener.open(request)
print response.read()
