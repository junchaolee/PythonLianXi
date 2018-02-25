#coding:utf-8
import requests
from bs4 import BeautifulSoup
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#由于python默认调用的是ascii编码解码处理字符流，所以下面使用utf-8将数据写入文件时会报错
'''
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment 
'''

html='https://movie.douban.com/top250?start=25&filter='
r=requests.get(html)
content=r.text
soup=BeautifulSoup(content,'html.parser')#指定解析器，也可以不指定，由自动选择，将固定的文档传入Beautiful构造方法
# print soup.prettify()
# print soup.title
# print soup.title.name
# print soup.title.string
# print soup.title.parent.name
# print soup.p
# print soup.a
# print soup.find_all('a')

#从文档中找出所有<a>标签的连接
# for link in soup.find_all('a'):
#     print link.get('href')

movieList=soup.find('ol',attrs={'class':'grid_view'})
# print movieList
for movieLi in movieList.find_all('li'):
    # print movieLi
    data=[] #定义一个空列表用来存储数据
    #得到电影的名字
    movieHd = movieLi.find('div', attrs={'class': 'hd'})  # 找到第一个class属性值为hd的div标签
    movieName = movieHd.find('span', attrs={'class': 'title'}).getText()  # 找到第一个class属性值为title的span标签
    # 也可使用.string方法
    # print movieName
    data.append(movieName)

    #得到电影评分
    movieScore=movieLi.find('span',attrs={'class':'rating_num'}).getText()
    # print movieScore
    data.append(movieScore)

    #得到电影发行的年份
    movieDe=movieLi.find('div',attrs={'class':'bd'})
    movieYe=movieDe.find('p',attrs={'class':''}).getText()
    movieYear=re.findall(r'\d+', movieYe)
    # print movieYear
    for i in movieYear:
        # print i
        data.append(i)


    #得到电影评价人数
    movieEval = movieLi.find('div', attrs={'class': 'star'})
    movieEvalNum = re.findall(r'\d+', str(movieEval))[-1]
    # print movieEvalNum
    data.append(movieEvalNum)

    #得到电影的短评
    movieQuto=movieLi.find('span',attrs={'class':'inq'})
    # print movieQuto
    if(movieQuto):
        data.append(movieQuto.getText())
    else:
        data.append("无")



    #将输出重定向到txt文件
    output=sys.stdout#保存标准输出流
    outputfile=open("movie.txt",'a')
    sys.stdout=outputfile#标准输出重定向到文件movie.txt
    # print data[0], data[1],data[2],data[3]

    #设定输出的格式
    # outputMode= "{0:{4}^20}\t{1:^10}\t{2:^10}\t{3:{4}<10}"
    outputMode = "{0:^30}\t{1:^10}\t{2:^10}\t{3:^10}\t{4}"
    # print(outputMode.format('电影名称', '评分', '评论人数', '短评'))
    print outputMode.format(data[0], data[1], data[2], data[3],data[4])

    outputfile.close()
    sys.stdout=output#恢复标准输出流
