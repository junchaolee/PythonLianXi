#coding:utf-8
import urllib2
import urllib
import time
import re

#定义函数，解析html中包含有图片的链接，结果为images列表
def parase_html(url,page):
    p1=page
    #伪装成浏览器的header
    send_headers={
    'Host':'jandan.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
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
    print images
    #调用get_imageurl_andsave函数生成带http的新的列表
    # get_imageurl_andsave(images,p1)

#加http
def get_imageurl_andsave(images,page):
    p2=page
    for i in range(len(images)):
        image = 'http:' + images[i]
        save_image(image,p2,i)

#利用url.urlretrieve保存图片至本地
def save_image(image,page,count):
    p3=page
    cnt=count
    save_path = "D:\\jiandan\\" +str(p3)+ str(cnt) + ".jpg"
    save_path = "D:\\jiandan\\" +str(p3)+ str(cnt) + ".jpg"
    print("下载第"+str(p3)+"页" + "第"+str(cnt) + "张照片")
    print("保存地址为:" + save_path)
    # 通过urllib模块中的urlretrieve保存图片
    urllib.urlretrieve(image, filename=save_path)
    time.sleep(1)

#python的主程序
if __name__=="__main__":
    p=30
    for x in range(20,p+1):
        print x
        url = "http://jandan.net/ooxx/page-" + str(x)
        parase_html(url,x)
        time.sleep(5)
