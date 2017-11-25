#coding:utf-8
import threading
import time

def sing():
    for i in range(3):
        print '正在唱歌...%d'%i
        time.sleep(1)

def dance():
    for i in range(3):
        print '正咋跳舞...%d'%i
        time.sleep(1)

if __name__=='__main__':
    print '-------开始-------:%s'%time.ctime()

    t1=threading.Thread(target=sing)
    t2=threading.Thread(target=dance)

    t1.start()
    t2.start()

    time.sleep(5)

    print '-------结束-------:%s'%time.ctime()


