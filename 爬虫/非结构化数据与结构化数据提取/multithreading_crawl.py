#coding:utf-8

import requests
from lxml import etree
from Queue import Queue
import threading
import time
import json

class thread_crawl(threading.Thread):
    '''
    抓取线程类
    '''

    def __init__(self,threadID,q):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.q=q

    def run(self):
        print "Starting:"+self.threadID
        self.qiushi_spider()
        print "Exiting:",self.threadID

    def qiushi_spider(self):
        pass

def main():
    pass


if __name__=='__main__':
    main()

