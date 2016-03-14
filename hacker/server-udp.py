# *-* coding:utf-8 *-*
import os
import socket, threading

bind_ip = '0.0.0.0'
bind_port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip, bind_port))

print('[*] Listening on %s:%d' %(bind_ip, bind_port) )

    

while True:
    request = server.recv(1024)
    print('[*] Received %s' %(request) )

