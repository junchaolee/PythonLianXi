#coding:utf-8
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas

pattern = re.compile(ur'[\u4e00-\u9fa5]+')
str1 ='脚本之家'
text=re.findall(pattern,str1)
print text
for i in text:
    print i

# [u'\u811a\u672c\u4e4b\u5bb6']
# [u'\u811a\u672c\u4e4b\u5bb6']