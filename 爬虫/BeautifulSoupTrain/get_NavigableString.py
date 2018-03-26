#coding:utf-8
from bs4 import BeautifulSoup

html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#create Beautiful Soup object,并指定特定的解析器，否则会警告提示用lxml
soup=BeautifulSoup(html,'html.parser')

#获取标签内部的文字.string
print soup.p.string
print type(soup.p.string)#<class 'bs4.element.NavigableString'>

#Comment 对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号
print soup.a.string
print type(soup.a.string)