#coding:utf-8
class Money(object):
    def __init__(self):
        self.__money=0

    def getMoney(self):
        return self.__money

    def setMoney(self,value):
        if isinstance(value,int):
            self.__money=value
        else:
            print 'error:不是整形数字'


m1=Money()
m1.setMoney(45)
print m1.getMoney()

m1.setMoney('456')
print m1.getMoney()