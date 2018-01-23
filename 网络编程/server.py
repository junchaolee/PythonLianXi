# coding:utf8

import socket   #socket模块
from time import ctime
import commands   #执行系统命令模块


BUF_SIZE = 1024  #设置缓冲区大小
server_addr = ('127.0.0.1', 8888)  #IP和端口构成表示地址
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #生成一个新的socket对象
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #设置地址复用
server.bind(server_addr)  #绑定地址
server.listen(5)  #监听, 最大监听数为5
while True:
    client, client_addr = server.accept()  #接收TCP连接, 并返回新的套接字和地址
    print 'Connected by', client_addr
    while True :
        data = client.recv(BUF_SIZE)  #从客户端接收数据
        print data
        client.sendall('[%s]%s'%(ctime(),data))  #发送数据到客户端
server.close()