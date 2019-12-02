import socket
import _thread

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

global control

ls = [0]
control = 0
new = 0
control1 = 0
#VERSION 1: Temporary functionality, thread terminates when p key is received
#define thread function
def controls (clientsocket, address):
	global control
	print(f"Connection from {address} established.")
	msg = clientsocket.recv(1)
	print(new)
	k = msg.decode("utf-8")
	print(k)
	while k != 'p':
		msg = clientsocket.recv(1)
		k = msg.decode("utf-8")
		control = k;

	print(f"{address} disconnected.")
	exit()

def listener ():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#AF_INET for IPV4. Use AF_INET6 for IPV6
	#SOCK_STREAM denotes TCP usage

	s.bind((socket.gethostname(),1230))
	#socket.gethostname() a temporary solution. only applies for same device communication
	#servers bind. clients connect.

	s.listen(5)
	#listening queue to handle multiple connections
	while True:
		clientsocket, address = s.accept()
		_thread.start_new_thread( controls, (clientsocket, address))	


_thread.start_new_thread( listener, ())

done = True
for step in range(50000):

	if done:
		state = env.reset()
	print(control)
	if control == 'd':
		print('1')
		ls[0] = 1 #1 is walk right
	elif control =='a':
		print('2')
		ls[0] = 8 #8 is walk left
	elif control =='m':
		print('4')
		ls[0] =4 #4 is jump right
	elif control =='w':
		print('3')
		ls[0] =5 # 5 is jump straight
	elif control =='s':
		print('2')
		ls[0] = 11 #useless so far?
	elif control == 'n':
		print('3')
		ls[0] =7 #7 is jump left
	action = ls[0]
    #action = env.action_space.sample()
    #print(action)
	control1 = 0
	state, reward, done, info = env.step(action)
	env.render()
	ls[0] =0
env.close()
