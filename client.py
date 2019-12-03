import pynput
import socket
import sys
import select
import tty
import time
import _thread

from pynput.keyboard import Key, Listener

run = 0
msg = 0

def on_press(key):
	global run
	global msg
	print('{0} pressed'.format(key))
	msg = format(key)
	print(msg)
	run = 1


def on_release(key):
	global run
	global msg
	print('{0} release'.format(key))
	run = 0
	if key == Key.esc:

        # Stop listener
		return False

def client():
	global run
	global msg
	ls = '0'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((socket.gethostname(),1269))	
	while 1:
		if run == 1:
			if msg == "'d'":
				#print('1')
				ls = '1' #1 is walk right
			elif msg =="'a'":
				#print('2')
				ls = '8' #8 is walk left
			elif msg =="'m'":
				#print('4')
				ls = '4' #4 is jump right
			elif msg =="'w'":
				#print('3')
				ls = '5' # 5 is jump straight
			elif msg =="'s'":
				#print('2')
				ls = '11' #useless so far?
			elif msg == "'n'":
				#print('3')
				ls ='7' #7 is jump left
			print(ls)
			s.send(bytes(ls, "utf-8"))
			if msg == "'p'":
				print("Disconnecting")
				break	
			time.sleep(0.01)		
		
#AF_INET = IPV4. Use AF_INET6 for IPV6
#SOCK_STREAM denotes TCP usage
_thread.start_new_thread( client, ())

while True:
# Collect events until released
	with Listener(on_press=on_press,on_release=on_release) as listener:
		listener.join()
		print("hi")




