# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

#自定义admin管理界面HeroInfo的子类
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','gender','hcontent']


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

#自定义admin管理界面BookInfo的子类
class BookInfoAdmin(admin.ModelAdmin):
    #显示字段
    list_display = ['id','btitle','bpub_date']
    #过滤字段
    list_filter = ['btitle']
    #搜索字段
    search_fields = ['btitle']
    #分页显示
    list_per_page = 5
    #属性分组
    fieldsets = [
        ('基本',{'fields':['btitle']}),
        ('高级',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline]

# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
