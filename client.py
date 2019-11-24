import socket
import sys
import select
import tty
import termios

#VERSION 1: Temporary functionality, client terminates when p key is pressed. 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = IPV4. Use AF_INET6 for IPV6
#SOCK_STREAM denotes TCP usage

s.connect((socket.gethostname(),1232))
while True:
	def isData():
		return select.select([sys.stdin],[],[],0) == ([sys.stdin],[],[])
	old_settings = termios.tcgetattr(sys.stdin)
	try:
		tty.setcbreak(sys.stdin.fileno())
		while 1:
			if isData():
				c = sys.stdin.read(1)	
				s.send(bytes(c, "utf-8"))
				#VERSION 1: Temporary functionality, send p key to server to allow it to terminate it's corresponding thread before terminating the client. 				
				if c == 'p':
					break


	finally:
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
		print("exiting game...")
		exit()


