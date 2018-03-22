#coding:utf-8
'''
finditer(self, string, pos=0, endpos=-1)
finditer 方法的行为跟 findall 的行为类似，也是搜索整个字符串，获得所有匹配的结果。但它返回一个顺序访问每一个匹配结果
Match 对象）的迭代器
'''

import re
pattern=re.compile(r'\d+')

result_iter=pattern.finditer('hello 123456 789')
# print type(result_iter)#<type 'callable-iterator'>
for m1 in result_iter:#m1是Match对象
    print 'Matching string:{},positon:{}'.format(m1.group(),m1.span())


'''
split(string[, maxsplit])
maxsplit 用于指定最大分割次数，不指定将全部分割
split 方法按照能够匹配的子串将字符串分割后返回列表
'''
p = re.compile(r'[\s\,\;]+')
print p.split('a,b;; c   d')