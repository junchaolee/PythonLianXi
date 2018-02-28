#coding:utf-8
import urllib
from bs4 import BeautifulSoup
import jieba
import pandas
import re
import numpy    #numpy计算包
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
# %matplotlib inline
import matplotlib
matplotlib.rcParams['figure.figsize']=(10.0,5.0)
from wordcloud import WordCloud#词云包
import warnings
warnings.filterwarnings('ignore')


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

# for i in play_list:
#     print i['id'],"---",i['name']

#对列表中第一部电影《红海行动》的评论进行分析
requrl = 'https://movie.douban.com/subject/' + play_list[2]['id'] + '/comments' +'?' +'start=0' + '&limit=20'
resp = urllib.urlopen(requrl)
html_data = resp.read().decode('utf-8')
soup = BeautifulSoup(html_data, 'html.parser')
comment_div_lits = soup.find_all('div', class_='comment')
# for i in comment_div_lits:
#     print i

eachCommonList=[]
for item2 in comment_div_lits:
    if item2.find_all('p')[0].string is not None:
        # print item2.find_all('p')[0].string
        eachCommonList.append(item2.find_all('p')[0].string)

comments=''
for k in range(len(eachCommonList)):
    comments+=str(eachCommonList[k]).strip()#系统默认界面是ascii,中文则需要使用utf-8,设置系统编码方式
    # print comments

#数据清洗，去除标点符号
filtercomments=re.sub('，|：|…|、|！|；|。|？|\d|\+|《|》|\.',"",comments)
# print filtercomments

#分词
segment=jieba.lcut(filtercomments)
words_df=pandas.DataFrame({'segment':segment})
# print words_df.head(10)

#去掉一些虚词
stopwords =pandas .read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],encoding='utf-8')  # quoting=3全不引用
words_now = words_df[~words_df.segment.isin(stopwords.stopword)]
# print words_now.head(10)

#统计每个词的频率
words_stat=words_now.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)
# print words_stat.head(10)

wcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)  # 指定字体类型、字体大小和字体颜色
word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
word_frequence_list = []
for key in word_frequence:
    temp = (key, word_frequence[key])
    word_frequence_list.append(temp)

# wcloud = wcloud.fit_words(word_frequence_list)
wcloud=wcloud.fit_words(dict(word_frequence_list))
plt.imshow(wcloud)
plt.savefig("result.jpg")