#-*-coding:utf-8 -*-
class Car:
    def __init__(self,newWheelNum,newColor):
        self.wheelNum=newWheelNum
        self.color=newColor

    def move(self):
        print '车在跑，目标：上海'


BMW=Car(7,'green')


print '车的颜色'+BMW.color
print '车的轮胎数量'+str(BMW.wheelNum)
