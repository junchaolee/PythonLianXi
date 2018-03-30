#coding:utf-8
"""
作为一名爬虫工程师，你最需要关注的，是数据的来源
获取Ajax异步加载的内容

做爬虫最需要关注的不是页面信息，而是页面信息的数据来源
Ajax方式加载的页面，数据一定是JSon
拿到JSon就拿到了数据的来源
"""

import urllib
import urllib2

url=""
ua_headers={
    "User-Agent":""
}

formdata