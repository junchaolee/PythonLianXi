#coding:utf-8
# src="//wx1.sinaimg.cn/mw600/5d3ea51egy1flbjranrrsj20u011itas.jpg"
import urllib2
import urllib
import time
import re

#要爬取的网页url
url='http://jandan.net/ooxx/page-28'

#伪装成浏览器的header
send_headers={
    'Host':'jiandan.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive'
}

#通过urllib2的Requst发起请求，加headers参数
request=urllib2.Request(url,headers=send_headers)
response=urllib2.urlopen(request)
#解析出爬取的网页html
html=response.read()
print html
#通过正则表达式解析出image列表
images=re.findall(r'src="(.*?\.jpg)"',html)
# print images
for i in range(len(images)):
    image = 'http:' + images[i]
    save_path = "E:\\jiandan\\" + str(i) + ".jpg"
    print("下载第"+str(i)+"张照片")
    print("保存地址为:"+save_path)
    #通过urllib模块中的urlretrieve保存图片
    urllib.urlretrieve(image, filename=save_path)
    # time.sleep(2)