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
            print 'err:不是整数数字'



