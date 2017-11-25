# -*-coding:utf-8 -*-

class base(object):
    def test(self):
        print '-----base test-----'

class A(base):
    def test(self):
        print  '------A test------'


#定义一个父类
class B(base):
    def test(self):
        print '-----B test -------'

#定义一个子类，继承自A、B
class C(A,B):
    pass


obj_C=C()
obj_C.test()

print C.__mro__
