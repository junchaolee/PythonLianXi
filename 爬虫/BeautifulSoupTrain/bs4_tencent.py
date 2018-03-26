#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import urllib
import json #使用了json格式存储

def tencent():
    url="https://hr.tencent.com/position.php?&start=10#a"
    # kw={"start":"0"}
    # print  urllib.urlencode(kw)
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    resHtml=response.read()
    print resHtml





if __name__=='__main__':
    tencent()