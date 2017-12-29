#-*-coding:utf-8-*-
class Itcast(object):
    def __init__(self,subject1):
        self.subject1=subject1
        self.subject2='cpp'

    #属性拦截器，可以打印log
    def __getattribute__(self, item):
        if item=='subject1':
            print 'log subject1'
            return 'redirect python'
        else:
            return object.__getattribute__(self,item)

    def show(self):
        print 'this is Itcast'

s=Itcast('python')
print s.subject1
print s.subject2