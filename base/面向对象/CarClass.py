# -*-coding:utf-8 -*-
class Car:
    def __init__(self):
        self.wheelNum=4
        self.color='蓝色'
    def move(self):
        print '车在奔跑，目标：上海'


BMW=Car()

print '车的颜色'+BMW.color
print '车的轮胎数量'+str(BMW.wheelNum)