#coding:utf-8
import urllib,urllib2,cookielib,string
from PIL import Image
def getchk(number):
    #create cookie object
    cookie=cookielib.LWPCookieJar()
    cookieSupport=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(cookieSupport,urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    #first connect to web and get cookies
    #act as browser
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'
    }

    reqO=urllib2.Request(
        url='http://mis.teach.ustc.edu.cn',
        headers=headers
    )

    #捕捉http错误
    try:
        resultO=urllib2.urlopen(reqO)
    except urllib2.HTTPError,e:
        print e.code

    #提取cookie
    getcookie = ['', ]
    for item in cookie:
        getcookie.append(item.name)
        getcookie.append("=")
        getcookie.append(item.value)
        getcookie=''.join(getcookie)

    #修改headers
    headers["Origin"] = "http://mis.teach.ustc.edu.cn"
    headers["Referer"] = "http://mis.teach.ustc.edu.cn/userinit.do"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Cookie"] = getcookie

    for i in range(number):
        req=urllib2.Request(
            url="http://mis.teach.ustc.edu.cn/randomImage.do?date='1469451446894'",
            headers=headers
        )
        response=urllib2.urlopen(req)
        status=response.getcode()
        picData=response.read()
        if status==200:
            localPic=open("./source/"+str(i)+".jpg","wb")
            localPic.write(picData)
            localPic.close()
        else:
            print "获取验证码失败"



if __name__=="__main__":
    getchk(10)