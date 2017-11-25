# -*-coding:utf-8 -*-

import time
class Animal(object):
    #初始化方法
    #创建完对象后会自动被调用
    def __init__(self,name):
        print '__init__方法被调用'
        self.__name=name

    #析构方法
    #当对象被删除是，会自动被调用
    def __del__(self):
        print '__del__方法被调用'
        print '%s对象马上被干掉..'%self.__name

#创建对象
dog=Animal('哈皮狗')

#删除对象
del dog

cat=Animal('波斯猫')
cat2=cat
cat3=cat

print '---------马上删除cat对象'
del cat
print '---------马上删除cat2对象'
del cat2
print '---------马上删除cat3对象'
del cat3

print '程序2秒钟后结束'
time.sleep(2)
