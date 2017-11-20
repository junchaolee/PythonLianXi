# -*-coding:utf-8 -*-
class SweetPotato:
    '这是烤地瓜的类'

    #定义初始化方法
    def __init__(self):
        self.cookedLevel=0
        self.cookedString='生的'
        self.condiments=[]

    #烤地瓜的方法
    def cook(self,time):
        self.cookedLevel+=time
        if self.cookedLevel>8:
            self.cookedString='烤成灰了'
        elif self.cookedLevel>5:
            self.cookedString='烤好了'
        elif self.cookedLevel>3:
            self.cookedString='半生不熟'
        else:
            self.cookedString='生的'


mySweetPotato=SweetPotato()
print mySweetPotato.cookedLevel
print mySweetPotato.cookedString
print mySweetPotato.condiments
print '-------------接下来要进行烤地瓜------------'
mySweetPotato.cook(4)
print mySweetPotato.cookedLevel
print mySweetPotato.cookedString
