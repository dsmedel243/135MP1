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

def test(event):
    if event.name == 'right':
        ls.append(0)

def on_release(key):
	print('{0} pressed'.format(key))

	if key == Key.esc:
		return False

done = True
for step in range(50000):

    if done:
        state = env.reset()
        
    if keyboard.is_pressed('d'):
        print('1')
        ls[0] = 1 #1 is walk right
    elif keyboard.is_pressed('a'):
        print('2')
        ls[0] = 8 #8 is walk left
    elif keyboard.is_pressed('m'):
        print('4')
        ls[0] =4 #4 is jump right
    elif keyboard.is_pressed('w'):
        print('3')
        ls[0] =5 # 5 is jump straight
    elif keyboard.is_pressed('s'):
        print('2')
        ls[0] = 11 #useless so far?
    elif keyboard.is_pressed('n'):
        print('3')
        ls[0] =7 #7 is jump left
    
    action = ls[0]
    #action = env.action_space.sample()
    print(action)

    state, reward, done, info = env.step(action)
    env.render()
    ls[0] =0
env.close()
