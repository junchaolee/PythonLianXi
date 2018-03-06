#coding:utf-8
class Test():
    def __init__(self):
        self.__num=100

    def setNum(self,newNum ):
        self.__num=newNum

    def getNum(self):
        return self.__num

    num=property(getNum,setNum)

t=Test()
print t.getNum()
print '-'*10
t.num=200
print t.num