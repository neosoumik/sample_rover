#!/usr/bin/python

import socket
x=0

while 1>0:
	s = socket.socket()
	host = socket.gethostname()
	port = 12316
	s.connect((host, port))
	print(s.recv(1024))
	x=x+1
	print (x)

	s.close
