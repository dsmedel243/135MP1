# 135MP1
## Coe 135 Project 1stSY1920

Collaborators: 
Larry Garriz, Mae Mabanta, Danica Medel


## Server Program:
The Server program collects inputs from connected client programs and sends them into a queue for the Super Mario Bros game to use as input. This is achieved through multithreading and mutex lock implementations. The Server is also responsible for rendering the game window and game output can only be viewed on the machine running the server. 

#### Setting up
Download mserver.py and make sure libraries have been installed.
#### Running Server program
On the terminal, run the following: `python mserver.py <IP address>`
#### Libraries used: 
Nes-Py
Super Mario Bros OpenAI Gym 




## Client Program
The client program is the main user interface of this project. Inputs to the game are typed into the terminal, and connection to the server (as well as the client itself) are terminated using the 'p' key.

#### Running Client program
On the terminal, run the following: `python client.py <IP address>`

Note: The IP address must be the IP address of the Server program. 
#### Setting up
Download client.py and make sure libraries have been installed.
#### Libraries used:
Pynput `on_release` and `on_pressed`
Termios

#### Client Controls

| Keyboard input| Action        |
| ------------- |:-------------:|
| w | jump      |
| s | crouch    |
| a | left      |
| d | right     |
| p | exit      |

#### OS Limitations
This program could be run only on Linux. Termios on the client program is limited to Unix users only. 

## References
[Twitch Plays Pokemon](https://www.twitch.tv/twitchplayspokemon)

```
@misc{gym-super-mario-bros,
  author = {Christian Kauten},
  howpublished = {GitHub},
  title = {{S}uper {M}ario {B}ros for {O}pen{AI} {G}ym},
  URL = {https://github.com/Kautenja/gym-super-mario-bros},
  year = {2018},
}
```

