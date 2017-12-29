#coding:utf-8
"""
单例模式是指:保证一个类仅有一个实例，并提供一个访问它的全局访问点
单例模式的优点：
1、由于单例模式要求在全局内只有一个实例，因而可以节省比较多的内存空间；
2、全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用；
3、单例可长驻内存，减少系统开销。
单例模式的应用举例：
1、生成全局惟一的序列号；
2、访问全局复用的惟一资源，如磁盘、总线等；
3、单个对象占用的资源过多，如数据库等；
4、系统全局统一管理，如Windows下的Task Manager；
5、网站计数器。
"""

import threading
import time

#使用方法__new__来实现单例模式
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls,'_instance'):
            orig=super(Singleton, cls)
            cls._instance=orig.__new__(cls,*args,**kw)
        return cls._instance

#总线
class Bus(Singleton):
    lock=threading.RLock()
    def sendData(self,data):
        self.lock.acquire()
        time.sleep(3)
        print "sending signal Data...",data
        self.lock.release()

#线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus=""
    name=""
    def getName(self):
        return self.name

    def setName(self, name):
        self.name=name

    def run(self):
        self.my_bus=Bus()
        self.my_bus.sendData(self.name)

if __name__=="__main__":
    for i in range(3):
        print 'Entity %d begin to run ...'%i
        my_entity=VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()