# -*- coding:utf-8 -*-

i=1
while i<=9:
    j=1
    while j<=i:
        print '%d*%d=%-4d'%(j,i,i*j),
        j+=1
    print '\n'
    i+=1