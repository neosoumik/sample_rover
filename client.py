#!/usr/bin/python

import socket
x=0

while 1>0:
	s = socket.socket()
	host = socket.gethostname()
	port = 118
	s.connect(('192.168.43.202', port))
	print(s.recv(1024))
	x=x+1
	print (x)

	s.close
