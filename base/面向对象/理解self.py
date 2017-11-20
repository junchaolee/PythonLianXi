# -*- coding:utf-8 -*-

class Animal:
    def __init__(self,name):
        self.name=name

    def printName(self):
        print '名字为:%s'%self.name


#定义一个函数`
def myPrint(animal):
    animal.printName()

dog1=Animal('西西')
myPrint(dog1)

dog2=Animal('北北')
myPrint(dog2)