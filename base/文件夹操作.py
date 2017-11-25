# -*- coding:utf-8 -*-

import os
#创建文件夹
# os.mkdir("jiandan")

#获取当前目录
cr=os.getcwd()
print cr

#改变默认目录
# os.chdir('D:\')

#获取目录列表
ls=os.listdir('./')
print ls

#删除文件夹
os.rmdir("jiandan")