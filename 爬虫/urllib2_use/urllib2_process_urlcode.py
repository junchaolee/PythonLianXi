#coding:utf-8
'''
urllib处理URL编码格式
'''
import urllib
import urllib2

url="http://www.baidu.com/s"
word={"wd":"手拉手"}
word_serch=urllib.urlencode(word)
new_url=url+"?"+word_serch
# print new_url

ua_header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
request=urllib2.Request(new_url,headers=ua_header)
response=urllib2.urlopen(request)
html=response.read()
print html