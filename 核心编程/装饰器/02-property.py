#coding:utf-8
class Test():
    def __init__(self):
        self.__num=100
    @property
    def num(self):
        return self.num

    @num.setter
    def num(self,newNum):
        self.__num=newNum
t=Test()
t.num=200
print t.num