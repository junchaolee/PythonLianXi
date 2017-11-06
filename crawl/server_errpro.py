#coding:utf8
import sys
import socket
from time import ctime
BUF_SIZE=1024
server_addr=('127.0.0.1',8888)
try:
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
    print "Socket创建失败，错误码: "+str(msg[0])+" 信息: "+msg[1]
    sys.exit()
print "创建成功!"

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)   #设置地址复用

try:
    server.bind(server_addr)
except socket.error,msg:
    print "绑定失败，错误代码:"+str(msg[0])+" 信息:"+msg[1]
    sys.exit()
print "绑定成功"

server.listen(5)
print "正在监听..."
while True:
    client,client_addr=server.accept()
    print "连接来自:",client_addr
    while True:
        data=client.recv(BUF_SIZE)
        print data
        client.sendall('[%s] %s'%(ctime(),data))
server.close()
