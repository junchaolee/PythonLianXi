#coding:utf-8
from threading import Thread,Lock
from time import sleep

class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print '----Task 1----'
                sleep(1)
                lock2.release()

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print '----Task 2----'
                sleep(1)
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print '----Task 3----'
                sleep(1)
                lock1.release()

#使用Lock创建的锁默认并没有锁上
lock1=Lock()
#创建另外一把锁，并且锁上
lock2=Lock()
lock2.acquire()
#创建另外一把锁，并且锁上
lock3=Lock()
lock3.acquire()

if __name__=='__main__':
    t1=Task1()
    t2=Task2()
    t3=Task3()
    t1.start()
    t2.start()
    t3.start()