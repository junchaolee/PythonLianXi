#coding:utf-8
import threading
import time
def saySorry():
    print '对不起，我错了，我可以吃饭了吗？'
    time.sleep(1)

if __name__=='__main__':
    for i in range(5):
        t=threading.Thread(target=saySorry)
        t.start()