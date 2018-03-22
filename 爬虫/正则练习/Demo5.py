#coding:utf-8
'''\
匹配中文：
    中文的 unicode 编码范围 主要在 [u4e00-u9fa5]，这里说主要是因为这个范围并不完整，
    比如没有包括全角（中文）标点，不过，在大部分情况下，应该是够用的。
'''
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

pattern = re.compile(ur'[\u4e00-\u9fa5]+')
str1 =u'你好，hello，世界'#别忘了加u
result=pattern.findall(str1)
print result
print result[0],result[1]



