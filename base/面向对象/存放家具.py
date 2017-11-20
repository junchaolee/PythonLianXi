# -*-coding:utf-8 -*-
class Home:

    def __init__(self,area):
        self.area=area
        self.light='on'#灯默认是亮的
        self.containsItem=[]

    def __str__(self):
        msg='当前房间可用面积为:'+str(self.area)
        if len(self.containsItem)>0:
            msg=msg+'容纳的物品有:'
            for temp in self.containsItem:
                msg=msg+temp.getName()+','
            msg=msg.strip(',')
        return msg

    #容纳物品
    def accommodateItem(self,item):
        #如果可用面积大于物品的占用面积
        needArea=item.getUsedArea()
        if self.area>needArea:
            self.containsItem.append(item)
            self.area-=needArea
            print 'ok:已经存放到房间中'
        else:
            print 'err:房间中可用面积为:%d,但是当前要存放的物品需要的面积为%d'%(self.area,needArea)


#定义bed类
class Bed:

    def __init__(self,area,name='床'):
        self.name=name
        self.area=area

    def __str__(self):
        msg='床的面积为:'+str(self.area)
        return msg

    #获取床的占用面积
    def getUsedArea(self):
        return self.area
    def getName(self):
        return self.name


#创建一个新家对象
newHome=Home(100)
print newHome

#创建一个床的对象
newBed=Bed(20)
print newBed

#吧床安放到家里
newHome.accommodateItem(newBed)
print newHome

#再次创建一个床的对象
newBed2=Bed(30,'席梦思')
print newBed2

#再次把床安放到家里
newHome.accommodateItem(newBed2)
print newHome