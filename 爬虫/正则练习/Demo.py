#coding:utf-8
"""
re 模块的一般使用步骤如下：
    1、使用 compile() 函数将正则表达式的字符串形式编译为一个 Pattern 对象
    2、通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得匹配结果，一个 Match 对象。
        match 方法：从起始位置开始查找，一次匹配
        search 方法：从任何位置开始查找，一次匹配
        findall 方法：全部匹配，返回列表
        finditer 方法：全部匹配，返回迭代器
        split 方法：分割字符串，返回列表
        sub 方法：替换

    3、最后使用 Match 对象提供的属性和方法获得信息，根据需要进行其他的操作

"""
import re
a="hello python 2018 03 22 hello"
#将正在表达式编译成pattern对象
# pattern=re.compile(r'\d+')
# m=pattern.match(a,13,50)#返回一个Match对象
# print m.group(0)
# print m.start()
# print m.end()
# print m.span()

pattern1=re.compile(r'([a-z]+) ([a-z]+)',re.I)#re.I忽略大小写
m1=pattern1.match("Hello World Wide Web")
print m1
print m1.group()
print m1.group(1)
print m1.group(2)
print m1.span(1)
print m1.span(2)
print m1.groups()#等价于(m1.group(1),m2.group(2),...)