# -*-coding:utf-8 -*-
oldFileName=raw_input("请输入要拷贝文件的名字:")
oldFile=open(oldFileName,'r')

if oldFile:
    fileFlagNum=oldFileName.rfind('.')
    # print fileFlagNum
    if fileFlagNum>0:
        fileFlag=oldFileName[fileFlagNum:]
        # print fileFlag

    newFileName=oldFileName[:fileFlagNum]+'[复制]'+fileFlag
    newFile=open(newFileName,'w')

    for lineContent in oldFile.readlines():
        newFile.write(lineContent)

    oldFile.close()
    newFile.close()

