#coding:utf-8
import urllib2
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider:
    '''
    内涵段子爬虫类
    '''
    def loadPage(self,page):
        '''
        @brief 定义一个url请求网页的方法
        :param page:
        :return:
        '''
        url="http://www.neihanpa.com/article/list_5_"+str(page)+".html"
        ua_header={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0"}
        # request=urllib2.Request(url,headers=ua_header)
        # response=urllib2.urlopen(request)
        # html=response.read()
        # print html
        response=requests.get(url,headers=ua_header)
        html=response.text
        gbk_html=html.decode('gbk').encode('utf-8')
        print gbk_html

if __name__=='__main__':
    mySpider=Spider()
    mySpider.loadPage(1)