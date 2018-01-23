# coding:utf8

import sys
import socket

BUF_SIZE=1024
server_addr=('127.0.0.1',8888)

try:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
    print "Socket创建失败，错误代码："+str(msg[0])+" 信息: "+msg[1]
    sys.exit()

client.connect(server_addr)

while True:
    data=raw_input("请输入要发送的信息:")
    if not data:
        print "输入不能为空，请重新输入.."
        continue
    client.sendall(data)
    data=client.recv(BUF_SIZE)
    print data
client.close()