#  -*-coding:utf-8 -*-
#定义一个父类
class Cat(object):

    def __init__(self,name,color='白色'):
        self.name=name
        self.color=color

    def run(self):
        print '%s--在跑'%self.name

#定义一个子类，继承Cat类
class Bosi(Cat):
    def setNewName(self,newName):
        self.name=newName

    def eat(self):
        print '%s--在吃'%self.name

bs=Bosi('印度猫')
print bs.name
print bs.color
bs.eat()
bs.setNewName('波斯')
bs.run()
