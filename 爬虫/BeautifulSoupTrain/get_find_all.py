#coding:utf-8
import re
from bs4 import BeautifulSoup
html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story2</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#create Beautiful Soup object,并指定特定的解析器，否则会警告提示用lxml
soup=BeautifulSoup(html,'html.parser')

#find_all(name, attrs, recursive, text, **kwargs)
#name参数：传入字符串、正则表达式、列表
print soup.find_all('b')

print '*'*50
for tag in soup.find_all(re.compile("^b")):
    print tag.name

print '*'*50
print soup.find_all(["a","b"])

#keywords参数
print '*'*50
print soup.find_all(id='link2')

#text参数
print'*'*50
print soup.find_all(text="Lacie")
print soup.find_all(text=["Lacie","Tillie"])
print soup.find_all(text=re.compile("Dormouse"))

#CSS选择器
#标签名查找
print'-'*50
print soup.select("title")
#类(class)名查找加.
print '-'*50
print soup.select(".sister")

#通过id名查找加#
print '-'*50
print soup.select("#link1")

#组合查找
print'-'*50
print soup.select('p #link2')
print soup.select('head > title')

#属性查找
print '-'*50
print soup.select('a[class=sister]')
print soup.select('a[href="http://example.com/elsie"]')

#通过get_text()获取内容
print '*'*50
print soup.select("title")[0].get_text()