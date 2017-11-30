#coding:utf-8
# def foo():
#     print 'foo'
#
# foo #表示是函数
# foo()#表示调用函数

def foo1():
    print 'foo1'

foo1=lambda x:x+1
foo1()#执行lambda表达式，而不是原来的foo1函数，因为foo1这个名字被重新指向了另外一个匿名函数