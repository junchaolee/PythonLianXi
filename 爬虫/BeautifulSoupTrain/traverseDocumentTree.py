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

#直接子节点 ：.contents .children 属性
#tag的.contents属性可以将tag的子节点以列表的方式输出
print soup.p.contents
print soup.p.contents[0]

print soup.p.children#list生成器对象
print '-'*50
#所有子孙节点.descendants
for child in soup.descendants:
    print child