#!/usr/bin/python
import socket
import sys

'''
#client
1. socket
2. port
3. connect
4. IO + close()
'''

clientSocket = []

if(len(sys.argv) < 3):
    print "Usage: client.py hostname portNumber"
else:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = sys.argv[1]
    port = int(sys.argv[2])
    connection = clientSocket.connect((host,port))
    clientSocket.recv(1024)
    clientSocket.close()

