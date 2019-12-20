#coding:utf-8
'''
利用BeautifulSoup解析html文档内容
思路分析:

'''
import requests
from bs4 import BeautifulSoup
import time
import re
import sys
reload(sys)
#由于python默认调用的是ascii编码解码处理字符流,在写入文件时会报错，所以需指定
sys.setdefaultencoding('utf-8')

#该函数用来解析要爬取的页面
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

#该函数利用BeautiSoup提取要获取的内容
def getData(html):
    soup=BeautifulSoup(html,'html.parser')
    movieList=soup.find('ol',attrs={'class':'grid_view'})#找到第一个class属性值为grid_view的ol标签

    for movieLi in movieList.find_all('li'):
        #定义一个空list用来存储数据
        data=[]
        #1、得到电影名字
        movieHd=movieLi.find('div',attrs={'class':'hd'})#找到第一个class属性值为hd的div标签
        movieName=movieHd.find('span',attrs={'class':'title'}).getText()#找到第一个class属性值为title的span标签
        data.append(movieName)

        #2、得到电影的评分
        movieScore=movieLi.find('span',attrs={'class':'rating_num'}).getText()
        data.append(movieScore)

        # 3、得到电影发行的年份
        movieDe = movieLi.find('div', attrs={'class': 'bd'})
        movieYe = movieDe.find('p', attrs={'class': ''}).getText()
        movieYear = re.findall(r'\d+', movieYe)
        # print movieYear
        for i in movieYear:
            data.append(i)

        # 4、得到电影评价人数
        movieEval = movieLi.find('div', attrs={'class': 'star'})
        movieEvalNum = re.findall(r'\d+', str(movieEval))[-1]
        # print movieEvalNum
        data.append(movieEvalNum)

        #5、 得到电影的短评
        movieQuto = movieLi.find('span', attrs={'class': 'inq'})
        # print movieQuto
        if (movieQuto):
            data.append(movieQuto.getText())
        else:
            data.append("无")

        #打印用于重定向输出写入到文件中
        print outputMode.format(data[0], data[1], data[2], data[3], data[4])

if __name__ == '__main__':
    #将结果输出到文件中
    output=sys.stdout#保存标准输出流
    outputfile=open('movie_top250_data_201912.txt','w')
    sys.stdout=outputfile#标准输出到moviedata.txt

    # 设定输出的格式
    # outputMode= "{0:{4}^20}\t{1:^10}\t{2:^10}\t{3:{4}<10}"
    outputMode = "{0:^30}\t{1:^10}\t{2:^10}\t{3:^10}\t{4}"
    print(outputMode.format('电影名称', '评分','年份', '评论人数', '短评'))
    basicUrl='https://movie.douban.com/top250'
    k=0
    while k<=225:
        html=getHTMLText(basicUrl,k)
        time.sleep(2)
        k+=25
        getData(html)
    outputfile.close()#关闭文件对象读写
    sys.stdout=output#恢复标准输出流


