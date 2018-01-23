# coding:utf8

import socket

BUF_SIZE=1024
server_addr=('127.0.0.1',8888)
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data=raw_input('Please Input data>: ')
    client.sendto(data,server_addr)
    data,addr=client.recvfrom(BUF_SIZE)
    print "Data:",data
client.close()

