#coding:utf-8

class Person(object):
    def __init__(self,name,age,taste):
        self.name=name
        self._age=age
        self.__taste=taste

    def showperson(self):
        print self.name
        print self._age
        print self.__taste

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):
        print 'my _work'

    def __away(self):
        print 'my __awy'

class Student(Person):
    def construction(self,name,age,taste):
        self.name=name
        self._age=age
        self.__taste=taste

    def showstudent(self):
        print self.name
        print self._age
        print self.__taste

    @staticmethod
    def testbug():
        _Bug.showbug()

class _Bug(object):
    @staticmethod
    def showbug():
        print 'showbug'

s1=Student('jack',25,'football')
s1.showperson()
print '*'*23
#无法访问__taste,导致报错
# s1.showstudent()
s1.construction('rose',34,'basketball')
s1.showperson()
print '#'*30
s1.showstudent()
print '^'*30
Student.testbug()

s1.dowork()