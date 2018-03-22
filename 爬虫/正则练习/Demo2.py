#coding:utf-8
"""
search 方法用于查找字符串的任何位置，它也是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果，.
它的一般使用形式如下：
search(string[, pos[, endpos]])
当匹配成功时，返回一个 Match 对象，如果没有匹配上，则返回 None。
"""
import re
pattern=re.compile(r'\d+')
# m=pattern.search('one12twothree34four')
# print m
# print m.group()
# m1=pattern.search('one12twothree34four',10,30)
# print m1.group()
# print m1.span()

'''
findall(string[, pos[, endpos]])
findall 以列表形式返回全部能匹配的子串，如果没有匹配，则返回一个空列表
'''
m2=pattern.findall('hello 123456 789')
m3=pattern.findall('one1two2three3four4', 0, 10)
print m2
print m3