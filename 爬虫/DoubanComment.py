#coding:utf-8
import warnings
warnings.filterwarnings("ignore")
import time
import jieba  # 分词包
import numpy  # numpy计算包
import codecs  # codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
import re
import pandas as pd
import matplotlib.pyplot as plt
import urllib
from bs4 import BeautifulSoup as bs
# % matplotlib inline
import matplotlib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud  # 词云包


# 分析网页函数
def getNowPlayingMovie_list():
    resp = urllib.urlopen('https://movie.douban.com/nowplaying/hangzhou/')
    html_data = resp.read().decode('utf-8')
    # print html_data#检测到有异常请求从你的 IP 发出
    soup = bs(html_data, 'html.parser')
    nowplaying_movie = soup.find_all('div', id='nowplaying')
    nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
    nowplaying_list = []
    for item in nowplaying_movie_list:
        nowplaying_dict = {}
        nowplaying_dict['id'] = item['data-subject']
        for tag_img_item in item.find_all('img'):
            nowplaying_dict['name'] = tag_img_item['alt']
            nowplaying_list.append(nowplaying_dict)
    return nowplaying_list


# 爬取评论函数
def getCommentsById(movieId, pageNum):
    eachCommentList = []
    if pageNum > 0:
        start = (pageNum - 1) * 20
    else:
        return False
    requrl = 'https://movie.douban.com/subject/' + movieId + '/comments' + '?' + 'start=' + str(start) + '&limit=20'
    # print requrl
    resp = urllib.urlopen(requrl)
    html_data = resp.read().decode('utf-8')
    # print html_data# <title>没有访问权限</title>
    soup = bs(html_data, 'html.parser')
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p')[0].string is not None:
            eachCommentList.append(item.find_all('p')[0].string)
            # print item.find_all('p')[0].string#这里显示的是正常的中文字符
    return eachCommentList


def main():
    # 循环获取第一个电影的前10页评论
    commentList = []
    NowPlayingMovie_list = getNowPlayingMovie_list()
    # for d in NowPlayingMovie_list:
    #     print d['id'],d['name']
    for i in range(10):
        num = i + 1
        commentList_temp = getCommentsById(NowPlayingMovie_list[0]['id'], num)
        print len(commentList_temp)
        commentList.append(commentList_temp)
        # print commentList[i][0]
        time.sleep(3)

    # 将列表中的数据转换为字符串
    comments = ''
    for k in range(len(commentList)):
        # print str(commentList[k][0])
        for m in range(len(commentList[k])):
            comments = comments + (str(commentList[k][m])).strip()
            # print comments

    # 使用正则表达式去除标点符号
    # pattern = re.compile(r'[\u4e00-\u9fa5]+')
    # filterdata = re.findall(pattern, comments)
    # cleaned_comments = ''.join(filterdata)
    cleaned_comments=re.sub('，|：|…|、|！|；|。|？|\d|\+|《|》|\.',"",comments)#自己写的，没用作者的
    # print cleaned_comments

    # 使用结巴分词进行中文分词
    segment = jieba.lcut(cleaned_comments)
    words_df = pd.DataFrame({'segment': segment})

    # 去掉停用词
    stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],encoding='utf-8')  # quoting=3全不引用
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

    # 统计词频
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)

    # 用词云进行显示
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)
    word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}

    word_frequence_list = []
    for key in word_frequence:
        temp = (key, word_frequence[key])
        word_frequence_list.append(temp)

    wordcloud = wordcloud.fit_words(dict(word_frequence_list))#加了个dict()
    plt.imshow(wordcloud)
    plt.savefig('result_comment.jpg')


# 主函数
main()