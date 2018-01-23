# coding:utf8

import sys
import socket


BUF_SIZE = 1024  #设置缓冲区的大小
server_addr = ('127.0.0.1', 8888)  #IP和端口构成表示地址
try :
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #返回新的socket对象
except socket.error, msg :
    print "Creating Socket Failure. Error Code : " + str(msg[0]) + " Message : " + msg[1]
    sys.exit()
client.connect(server_addr)  #要连接的服务器地址
while True:
    data = raw_input("Please input some string > ")
    if not data :
        print "input can't empty, Please input again.."
        continue
    client.sendall(data)  #发送数据到服务器
    data = client.recv(BUF_SIZE)  #从服务器端接收数据
    print data
client.close()