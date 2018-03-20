#coding:utf-8
#不要把packet名与要导入的包名相同
import pymysql.cursors
import json
'''
host:要连接的数据库的IP地址，如果是远程的，这里指定远程的ip地址
user：登录的账户名，如果登录的是最高权限账户则为root
password：对应的密码
db：要连接的数据库的名称，如需要访问存储的IRIS数据库，则输入'IRIS'
charset：设置编码格式，如utf8mb4就是一个编码格式
cursorclass：返回到Python的结果，以什么方式存储，如Dict.Cursor是以字典的方式存储
'''
#connect to the databases
connection=pymysql.connect(host='192.168.1.253',
                               user='root',
                               password='888888',
                               db='lijunchao',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql='select * from call_log order by start_time desc '
        cursor.execute(sql)
        result=cursor.fetchmany(20)
        # print json.dumps(result[0],ensure_ascii=False,encoding='UTF-8')
        for i in range(len(result)):
            print result[i].get('in_phone'),result[i].get('in_phone_location'),result[i].get('start_time')
            # print result[i].items()
            # print list(result[i].iteritems())
            # print result[i].keys()
    #commit之后才真正的进入数据库操作
    # connection.commit()
finally:
    connection.close()