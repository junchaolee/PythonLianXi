#coding:utf-8
import requests
from bs4 import BeautifulSoup
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
注意中文字符统一加u编码，否则会报错，爬不下去
错误:
    File "/Users/lijunchao/PycharmProjects/PythonLianXi/爬虫/Crawl_DoubanMovie.py", line 55, in getData
    print outputMode.format(data[0],data[1],data[2],data[3],unichr(12288))
    ValueError: Invalid conversion specification
'''

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
    movieList=soup.find('ol',attrs={'class':'grid_view'})#找到第一个class属性值为grid_view的ol标签


    for movieLi in movieList.find_all('li'):


        data=[]
        #得到电影名字
        movieHd=movieLi.find('div',attrs={'class':'hd'})#找到第一个class属性值为hd的div标签
        movieName=movieHd.find('span',attrs={'class':'title'}).getText()#找到第一个class属性值为title的span标签
        data.append(movieName.strip())

        #得到电影的评分
        movieScore=movieLi.find('span',attrs={'class':'rating_num'}).getText()
        data.append(movieScore)

        #得到电影的评价人数
        movieEval=movieLi.find('div',attrs={'class':'star'})
        movieEvalNum=re.findall(r'\d+',str(movieEval))[-1]
        data.append(movieEvalNum)

        #得到电影的短评
        movieQuote=movieLi.find('span',attrs={'class':'inq'})
        if(movieQuote):
            data.append(movieQuote.getText())
        else:
            data.append(u"无")#没有评论的都为无，并且得加上u，否则会报ValueError: Invalid conversion specification

        print outputMode.format(data[0],data[1],data[2],data[3],unichr(12288))


if __name__=='__main__':

    #将结果输出到文件中
    output=sys.stdout
    outputfile=open('moviedata.txt','w')
    sys.stdout=outputfile


    outputMode= "{0:{4}<20}\t{1:^10}\t{2:^10}\t{3:{4}<10}"#:后面的{4}表示宽度不够的用第5个参数填充，chr(12288)代表中文的空格
    print outputMode.format(u'电影名称',u'评分',u'评论人数',u'短评',unichr(12288))
    basicUrl='https://movie.douban.com/top250'
    k=0
    while k<=225:
        html=getHTMLText(basicUrl,k)
        time.sleep(2)
        k+=25
        getData(html)


    outputfile.close()
    sys.stdout=output


