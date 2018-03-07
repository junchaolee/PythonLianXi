# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import RequestContext,loader#导入模板包
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index1(request):
    # temp=loader.get_template('booktest/index1.html')
    # return HttpResponse(temp.render())#render()解析index1，将渲染的结果返回客户端
    #以上两行代码等同于下面一行
    # return render(request,'booktest/index1.html')
    #传数据
    context={'title':'123'}
    return render(request,'booktest/index1.html',context)

def index(request):
    bookList=BookInfo.objects.all()
    context={'info':bookList}
    return render(request,'booktest/index.html',context)

def show(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    context={'list':herolist}
    return render(request,'booktest/show.html',context)