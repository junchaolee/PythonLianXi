# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    # temp=loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    bookList=BookInfo.objects.all()
    context={'list':bookList}
    return render(request,'booktest/index.html',context)

def show(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    context={'list':herolist}
    return render(request,'booktest/show.html',context)