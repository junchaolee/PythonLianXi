#coding:utf-8
'''
随机添加/修改User-Agent
'''
import urllib2
import random

url="http://www.slswd.com"
ua_list=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
]

user_agent=random.choice(ua_list)
request=urllib2.Request(url)
#通过add_header添加一个特定的header
request.add_header("User-Agent",user_agent)
#查看header
read_header=request.get_header("User-agent")
response=urllib2.urlopen(request)
html=response.read()
print read_header