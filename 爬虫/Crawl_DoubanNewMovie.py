#coding:utf-8
import urllib
from bs4 import BeautifulSoup

#解析要爬取的页面，生成html字符串
response=urllib.urlopen('https://movie.douban.com/cinema/nowplaying/hangzhou/')
html_data=response.read().decode('utf-8')
# print html_data

#利用BeautifulSoup对信息进行提取
soup=BeautifulSoup(html_data,'html.parser')
movie_playing=soup.find_all('div',id='nowplaying')
movie_list=movie_playing[0].find_all('li', class_='list-item')
# print movie_list
# for i in movie_list:
#     print i['data-subject']

play_list = []
for item in  movie_list:
    playing_dict={}
    playing_dict['id']=item['data-subject']
    for tag_img_item in item.find_all('img'):
        # print tag_img_item['alt']
        playing_dict['name']=tag_img_item['alt']
        #将包含id、电影名称的字典数据放入列表中
        play_list.append(playing_dict)

for i in play_list:
    for j in i:
        print j['id'],j['name']
