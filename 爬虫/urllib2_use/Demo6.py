#coding:utf-8
'''
爬取百度贴吧
'''
import urllib
import urllib2
import time
import sys
reload(sys)
#由于python默认调用的是ascii编码解码处理字符流,在写入文件时会报错，所以需指定
sys.setdefaultencoding('utf-8')

def tieba_Spider(url,start_page,end_page):
    for page in range(start_page,end_page+1):
        pn=(page-1)*50
        ful_url=url+"&pn"+str(pn)
        # print ful_url
        filename=u"第"+str(page)+u"页.html"
        html=parse_page(ful_url,filename)
        save_file(html,filename)
        time.sleep(3)

def parse_page(url,filename):
    print '正在解析'+filename
    ua_header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
    request=urllib2.Request(url,headers=ua_header)
    response=urllib2.urlopen(request)
    return response.read()

def save_file(html,filename):
    print '正在保存'+filename
    with open(filename,'w') as f:
        f.write(html)
    print '-'*20

if __name__ == '__main__':
    kw=raw_input("请输入要爬取的贴吧：")
    #输入要爬取的起始页与终止页
    start_page=int(raw_input("起始页:"))
    end_page=int(raw_input("终止页:"))

    url="http://tieba.baidu.com/f?"
    search=urllib.urlencode({"kw":kw})
    new_url=url+search

    tieba_Spider(new_url,start_page,end_page)
