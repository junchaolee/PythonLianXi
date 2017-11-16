#coding:utf-8
f=open('text.txt','r')
str=f.read(10)
print '读取的内容是:',str
position=f.tell()
print "当前的位置是:",position

str=f.read(10)
print '读取的内容是:',str
position=f.tell()
print "当前的位置是:",position

#重新设置位置 seek(offset,from) 0:文件开头 1:当前位置  2:文件末尾
f.seek(5,0)
position=f.tell()
print "当前的位置是:",position


f.close()
