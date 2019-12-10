import socket
import _thread
import time
import queue
import sys
controlstack = queue.Queue(50)
from nes_py.wrappers import JoypadSpace
import random
import gym
from gym import spaces
import gym_super_mario_bros
import keyboard 

#from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, COMPLEX_MOVEMENT)

ls = [0]
control = 0

#controls is a dedicated thread that accepts connections from their respective connected clients and sends them into a mutex locked critical section
def controls (clientsocket, address):
	global controlstack
	global lock
	print(f"Connection from {address} established.")

	msg = clientsocket.recv(1)
	k = msg.decode('utf-8')
	while k != 4:
		msg = clientsocket.recv(1)
		k = int(msg.decode('utf-8'))
## CRITICAL SECTION ##
		if(lock.locked() != True):
			lock.acquire()
			#lock aquired			
			controlstack.put(int(k))	
			lock.release()	
			#lock released	
			
			#only the input of the thread with access will be pushed to the FIFO queue. inputs from other threads are 
			#discarded to prevent output bottleneck	
		if k == 4:
			print(f"{address} disconnected.")
			clientsocket.close()
			exit()			
	exit()

#the listener thread waits for new incoming connections. 
def listener ():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#AF_INET for IPV4. Use AF_INET6 for IPV6
	#SOCK_STREAM denotes TCP usage
	s.bind((sys.argv[1],6970))
	#servers bind. clients connect.
	s.listen()
	#listening queue to handle multiple connections
	while True:
		clientsocket, address = s.accept()
		_thread.start_new_thread( controls, (clientsocket, address))	

lock = _thread.allocate_lock()
_thread.start_new_thread( listener, ())


#game rendering loop 
done = True
for step in range(50000):
	if done:
		state = env.reset()
	if(controlstack.empty()):
		control = 0
	else:
		#control takes inputs from the FIFO queue
		control = controlstack.get()
		if control == 9:
			control = 10
	action = control
	control = 0
	state, reward, done, info = env.step(action)
	env.render()
env.close()
