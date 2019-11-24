import socket
import _thread

#VERSION 1: Temporary functionality, thread terminates when p key is received
#define thread function
def controls (clientsocket, address):
	print(f"Connection from {address} established.")
	msg = clientsocket.recv(1)
	k = msg.decode("utf-8")
	print(k)
	while k != 'p':
		msg = clientsocket.recv(1)
		k = msg.decode("utf-8")
		print(k)
	print(f"{address} disconnected.")
	exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET for IPV4. Use AF_INET6 for IPV6
#SOCK_STREAM denotes TCP usage

s.bind((socket.gethostname(),1232))
#socket.gethostname() a temporary solution. only applies for same device communication
#servers bind. clients connect.

s.listen(5)
#listening queue to handle multiple connections

while True: 
	clientsocket, address = s.accept()
	_thread.start_new_thread( controls, (clientsocket, address))
	#spawn new thread

