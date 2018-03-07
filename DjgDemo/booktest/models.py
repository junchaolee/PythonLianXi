# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#定义这个模型类的目的，创建数据表，还可以操作数据库进行增删改查
#模型类写完了要生成对应的迁移数据，生成迁移数据之前还有进行应用
#注册
# Create your models here.
class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField()
    def __str__(self):
        return self.btitle.encode('utf-8')

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    hbook=models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname.encode('utf-8')
