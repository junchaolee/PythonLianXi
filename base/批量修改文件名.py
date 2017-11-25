# -*- coding:utf-8 -*-

#批量在文件名前加前缀
import os

funFlag=1 #1.表示添加 2.表示删除

folderName='./Tmp/'

#获取指定路径的所有文件名
dirList=os.listdir(folderName)

#遍历出所有文件的名字
for name in dirList:
    print name

    if funFlag==1:
        newName='[Janus]-'+name
    elif funFlag==2:
        num=len('[Janus]-')
        newName=name[num:]
    print newName

    os.rename(folderName+name,folderName+newName)
