#coding:utf-8
from PIL import Image
I = Image.open('./source/1.jpg')
# I.show()
L = I.convert('L')   #转化为灰度图
L = I.convert('1')   #转化为二值化图
L.show()