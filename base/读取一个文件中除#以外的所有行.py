#-*- coding:utf-8 -*-
f=open('test.txt','r')
content=f.readlines()
for name in content:
    if name.find('#'):
        print name
    # print content

