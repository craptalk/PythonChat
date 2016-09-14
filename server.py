#!/usr/bin/python

import socket
import sys

"""
#server using TCP/IP
1. socket
2. port
3. bind
4. listen
5. accept
6. IO + close()
"""

recv_buffer=[1024]
servSocket = []
if(len(sys.argv)<3):
    print "Usage: server.py hostname portNumber"
    sys.exit()
else:
    servSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#using IPV4 protocol family
    host = sys.argv[1]
    port = int(sys.argv[2])

servSocket.bind((host, port))

servSocket.listen(10)

while 1:
    acc = servSocket.accept()
    print "Connection from ",acc
    servSocket.send("Hello it is server...")
    servSocket.close()