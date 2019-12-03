import socket
import _thread
import time

#from queue import LifoQueue
import queue
controlstack = queue.Queue()

from nes_py.wrappers import JoypadSpace
import random
import gym
from gym import spaces

import gym_super_mario_bros
import keyboard 

#from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v1')
env = JoypadSpace(env, COMPLEX_MOVEMENT)

ls = [0]
control = 0
new = 0


#VERSION 3: Temporary functionality, thread terminates when p key is received
#define thread function
def controls (clientsocket, address):
	global controlstack
	global new
	print(f"Connection from {address} established.")
	msg = clientsocket.recv(1)
	#print(new)
	k = msg.decode("utf-8")
	#print(k)
	while k != 'p':
		msg = clientsocket.recv(1)
		#new = 1
		k = msg.decode("utf-8")
		#control = k;
		controlstack.put(k)		
	print(f"{address} disconnected.")
	exit()

def listener ():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#AF_INET for IPV4. Use AF_INET6 for IPV6
	#SOCK_STREAM denotes TCP usage

	s.bind((socket.gethostname(),1269))
	#socket.gethostname() a temporary solution. only applies for same device communication
	#servers bind. clients connect.

	s.listen(5)#5 connections maximum for the server
	#listening queue to handle multiple connections
	while True:
		clientsocket, address = s.accept()
		_thread.start_new_thread( controls, (clientsocket, address))	


_thread.start_new_thread( listener, ())

done = True
for step in range(50000):

	if done:
		state = env.reset()

	if(controlstack.empty()):
		control = 0
	else:
		control = int(controlstack.get())
		#control = controlstack[0]
		#controlstack[0] = 0
		#controlstack = shift(-1, controlstack)
	print(control)

	action = control
    #action = env.action_space.sample()
    #print(action)
	control = 0
	state, reward, done, info = env.step(action)
	env.render()
	ls[0] =0
env.close()
