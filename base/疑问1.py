#coding:utf-8
"""
一个面试题：看下面代码会输出什么
"""

def extendList(val,list=[]):
    list.append(val)
    return list

list1=extendList(10)
print 'list1=%s'%list1
list2=extendList(234,['a','b','c'])
print 'list2=%s'%list2
list3=extendList('a')
print 'list3=%s'%list3
print 'list1=%s'%list1