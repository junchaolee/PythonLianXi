# -*-coding:utf-8 -*-
class Car:

    def __init__(self,newWheelNum,newColor):
        self.wheelNum=newWheelNum
        self.color=newColor

    def __str__(self):
        msg="嘿...我的颜色是"+self.color+"我有"+str(self.wheelNum)+"个轮胎..."
        return msg

    def move(self):
        print '车在跑，目标：上海'

BMW=Car(4,'白色')
print BMW