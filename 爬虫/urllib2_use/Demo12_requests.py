#coding:utf-8
"""
客户端验证
"""
import requests
auth=('sls','123123')

response=requests.get("http://192.168.1.253/nagios",auth=auth)

print response.text