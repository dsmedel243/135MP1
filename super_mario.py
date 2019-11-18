from nes_py.wrappers import JoypadSpace
import random
import gym
from gym import spaces

import gym_super_mario_bros
import keyboard 

#from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import RIGHT_ONLY
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, RIGHT_ONLY)

ls = [0]

def test(event):
    if event.name == 'right':
            ls.append(0)

done = True
for step in range(5000):

    if done:
        state = env.reset()

    if keyboard.is_pressed('right'):
        print('1')
        ls[0] = 1
    elif keyboard.is_pressed('left'):
        print('2')
        #ls.append(2)
        ls[0] = 2
    elif keyboard.is_pressed('up'):
        print('4')
        #ls.append(3)
        ls[0] = 4
    elif keyboard.is_pressed('down'):
        print('3')
        #ls.append(4)
        ls[0] =3

    #keyboard.on_release(test)
    #action = [0,0,0,1,1,1,1,1,1,2,3,3,2,2,1,1,1,1,1]
    #ls = ['NOOP']
    
    action = ls[0]
    #action = [['right'], ['right'],['right', 'A'], ['right', 'B'], ['right', 'A','B']]

    print(action)
    #env.action_spaces = spaces.Discrete(10)
    #action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    env.render()

env.close()