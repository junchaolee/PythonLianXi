#coding:utf-8
from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^(\d+)$',views.show)#只匹配数字
]
