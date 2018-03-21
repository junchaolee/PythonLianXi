#coding:utf-8
'''
urllib 仅可以接受URL，不能创建 设置了headers 的Request 类实例；

但是 urllib 提供 urlencode 方法用来GET查询字符串的产生，而 urllib2 则没有。（这是 urllib 和 urllib2 经常一起使用的主要原因）

编码工作使用urllib的urlencode()函数，帮我们将key:value这样的键值对转换成
"key=value"这样的字符串，解码工作可以使用urllib的unquote()函数。（注意，不是urllib2.urlencode() )

一般Http请求提交数据都要编码成URL编码格式，然后作为url的一部分，或者作为参数传给Request对象
'''
import urllib
word={"wd":"手拉手"}
print urllib.urlencode(word)
print urllib.unquote("wd=%E6%89%8B%E6%8B%89%E6%89%8B")