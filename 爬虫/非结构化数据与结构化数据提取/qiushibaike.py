#coding:utf-8
import requests
from lxml import etree

page=1
url='http://www.qiushibaike.com/8hr/page/'+str(page)

au_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
            "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
            }

try:
    response=requests.get(url,headers=au_headers)
    res_html=response.text
    html=etree.HTML(res_html)##利用etree.HTML,将字符串解析为HTML文档
    result=html.xpath('//div[contains(@id,"qiushi_tag")]')
    # print result

    for site in result:
        imgUrl=site.xpath('./div/a/img/@src')[0].encode('utf-8')
        # username=site.xpath('./div/a/@title')[0].encode('utf-8')#没有找到
        username=site.xpath('.//h2')[0].text.encode('utf-8')#text()方法获取元素内容
        content=site.xpath('.//div[@class="content"]/span')[0].text.strip().encode('utf-8')
        vote=site.xpath('.//i')[0].text.encode('utf-8')

        print "[头像路径:]http://"+imgUrl+"[用户名:]"+username,"[内容:]"+content,vote

except Exception,e:
    print e
