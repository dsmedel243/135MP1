import pynput
from pynput import keyboard
import socket
import sys
import select
import time
import _thread
import os

from pynput.keyboard import Key, Listener
from termios import tcflush, TCIFLUSH

run = 0
msg = 0
IP = '192.168.208.108'

w = 0
a = 0
ss = 0
d = 0
m = 0

def on_press(key):
	global msg 
	global run
	global w
	global a
	global ss
	global d
	global m

	#print('{0} pressed'.format(key))
	msg = format(key)
	if msg == "'w'":
		w = 1
		print(w)
	elif msg =="'a'":
		a = 1
	elif msg =="'s'":
		ss = 1
	elif msg =="'d'":
		d = 1
	elif msg =="'m'":
		m = 1

	#print(msg)
	#run = 1

def on_release(key):

	global run
	global w
	global a
	global ss
	global d
	global m

	if key == keyboard.Key.esc:
		return False

	#print('{0} release'.format(key))
	msg = format(key)
	if msg == "'w'":
		w = 0
		print(w)
	elif msg =="'a'":
		a = 0
		print(a)
	elif msg =="'s'":
		ss = 0
		print(ss)
	elif msg =="'d'":
		d = 0
		print(d)
	elif msg =="'m'":
		m = 0
		print(m)
	elif msg =="'p'":
		return False
	#run = 0
	#if key == Key.esc: #what's this again?
        # Stop listener
	#	return False

def client():
	#global run
	global msg
	global w
	global a
	global ss
	global d
	global m
	global listener
	ls = '0'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.2.118', 6970))

	while 1:
		if w==1 or a==1 or ss==1 or d==1 or m==1:
		#if run == 1:
			if w == 1:
				ls = 5 #5 jump
			elif a == 1:
				ls = 8 #8 left (+ fire)
			elif ss == 1:
				ls = 9 #10 crouch
			elif d == 1:
				ls = 3 #3 right (+ fire)
			elif m == 1:
				ls = 11
			if w == 1 and d == 1:
				ls = 2
			if w == 1 and a == 1:
				ls = 7
			#print(ls)
			s.send(str(ls).encode('utf-8'))
			time.sleep(0.01)

		if msg == "'p'":
			print("\nDisconnecting")
			msg = 4
			s.send(str(msg).encode('utf-8'))
			s.close()
			listener = ''
			tcflush(sys.stdin, TCIFLUSH)
			return False
			exit()	
			#return False

#AF_INET = IPV4. Use AF_INET6 for IPV6
#SOCK_STREAM denotes TCP usage
_thread.start_new_thread( client, ())

#while 1:
# Collect events until released
with Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()
