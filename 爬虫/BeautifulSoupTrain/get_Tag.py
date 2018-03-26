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
# print soup.title
# print soup.head
# print soup.a
print soup.p
# print type(soup.p)#<class 'bs4.element.Tag'>

#对于Tag，它有两个重要的属性，name和attrs
# print soup.name#soup对象的name比较特殊，为[document]
# print soup.head.name
# print soup.p.name
print soup.p.attrs
print soup.p['class']#等价于soup.p.get('class')

# soup.p['class']='newClass'#修改属性
# print soup.p

# del soup.p['class']#删除该属性
# print soup.p

#BeautifulSoup 对象表示的是一个文档的内容。大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag
print type(soup.name)
print soup.name
print soup.attrs