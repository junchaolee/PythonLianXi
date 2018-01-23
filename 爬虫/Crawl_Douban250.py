#coding:utf-8
import requests
from bs4 import BeautifulSoup
import time
import re
import sys

def getHTMLText(url,k):
    try:
        if(k==0):
            kw={}
        else:
            kw={'start':k,'filter':''}

        r=requests.get(url,params=kw,headers={'User-Agent': 'Mozilla/4.0'})
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print 'failed!'

def getData(html):
    soup=BeautifulSoup(html,"html.parser")
    movieList=soup.find('ol',attrs={'class':'grid_viw'})#找到第一个class属性值为grid_view的ol标签
    print movieList

    movieInfo=[]
    # for movieLi in soup.find_all('li'):
    #     print movieLi
    #     data=[]
    #     #得到电影名字
    #     movieHd=movieLi.find('div',attrs={'class':'hd'})#找到第一个class属性值为hd的div标签
    #     movieName=movieHd.find('span',attrs={'class':'title'}).getText()#找到第一个class属性值为title的span标签

        # data.append(movieName)
        # #得到电影的评分
        # movieScore=movieLi.find('span',attrs={'class':'rating_num'}).getText()
        # data.append(movieScore)
        #
        # #得到电影的评价人数
        # movieEval=movieLi.find('div',attrs={'class':'star'})
        # movieEvalNum=re.findall(r'\d+',str(movieEval))[-1]
        # data.append(movieEval)
        #
        # #得到电影的短评
        # movieQuote=movieLi.find('span',attrs={'class':'inq'})
        # if(movieQuote):
        #     data.append(movieQuote.getText())
        # else:
        #     data.append("无")
        #
        # print data[0],data[1],data[2],data[3]



#将结果输出到文件中
output=sys.stdout
outputfile=open('moviedata.txt','w')
sys.stdout=outputfile

basicUrl='https://movie.douban.com/top250'
k=0
while k<=225:
    html=getHTMLText(basicUrl,k)
    time.sleep(2)
    k+=25
    getData(html)


outputfile.close()
sys.stdout=output


