#-*-coding:utf-8 -*-
class Cat(object):
    def syaHello(self):
        print 'hello --1'

class Bosi(Cat):
    def syaHello(self):
        print 'hello --2'

bosi=Bosi()
bosi.syaHello()