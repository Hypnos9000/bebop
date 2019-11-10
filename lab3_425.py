
import sys
import os
import code
import readline
import rlcompleter
import socket
#import tty
#import argparse (if you want the 
import tkinter as tk

sys.path.append('../src')

from Bebop_Discovery import *
import Bebop_Device

print('Searching for devices')

#pip install untangle
#pip install zeroconf
#pip install pyparrot
#These 3 things need to be installed before you can run the yaw, roll, pitch after instlling these 3 we can try to import the multiple commands and libraries
# from pyparrot.Bebop import Bebop


#Script looks for drone on network
discovery = Discovery([DeviceID.BEBOP_DRONE, DeviceID.JUMPING_SUMO])


devices = discovery.get_devices()

#make into if statement, if drone is found on wifi
discovery.stop()

#NEED TO CREATE IF NOT CONNECT


device = next(iter(devices.values()))



#Need to edit: Bebop port found from sniffing packets from last HW2
d2c_port = 54321
controller_type = "PC"
controller_name = "bybop shell"

drone = Bybop_Device.create_and_connect(device, d2c_port, controller_type, controller_name)


vars = globals().copy()

vars.update(locals())

readline.set_completer(rlcompleter.Completer(vars).complete)

readline.parse_and_bind("tab: complete")

#Create an interactive shell that will be used to control the drone. 
shell = code.InteractiveConsole(vars)
#parser = argparse.ArgumentParser(description='Set parameters for Parrot Bebop2')
#parser.add_argument('-v', type = int, default = 20, help ='variable for roll, pitch, yaw')
#parser.add_argument('-d', type = int, default = 2, help ='duration for each key press')

#args = parser.parse_args()

#percentage = args.v
#duration_s = args.d
# this omitted code will allow us to change the parameter of percetage and duration whenever we run the code 
#Ask group members if they want to default it on a certain number
#Another tricky thing that may not be needed would be termious library since using that we are able to use an interactive termianl
#drone.flat_trim() unsure of exactly what this does however it may be using it as a reference. 
#A way to test this would be on 2 different Kali Linux modules 

def Keypress(press):

	if press.char == "t":
		text.insert('end', 'Taking off\n')
		drone.take_off()

	if press.char == "l":
		text.insert('end', 'Landing\n')
		drone.land()

	if press.char == "q":
		text.insert('end','Quit Terminal\n')
		drone.land()

	if press.char == "f":
		text.insert('end', 'Foward\n')
		drone.fly_direct(roll=0, pitch=percentage, yaw=0, vertical_movement=0, duration=duration_s)
		drone.flat_trim()

	elif press.char == "w":
		text.insert('end',"Left\n")
		drone.fly_direct(roll=-percentage, pitch=0, yaw=0, vertical_movement=0, duration=duration_s)
		drone.flat_trim()

	elif (char == "s"):
		text.insert('end',"Backward\n")
		drone.fly_direct(roll=0, pitch=-percentage, yaw=0, vertical_movement=0, duration=duration_s)
		drone.flat_trim()

	elif (char == "d"):
		text.insert('end',"Right\n")
		drone.fly_direct(roll=percentage, pitch=0, yaw=0, vertical_movement=0, duration=duration_s)
		drone.flat_trim()

	elif (char == "j"):
		text.insert('end',"Up\n")
		drone.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=percentage, duration=duration_s)
		drone.flat_trim()

	elif (char == "k"):
		text.insert('end',"Down\n")
		drone.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-percentage, duration=duration_s)
		drone.flat_trim()

	elif (char == "y"):
		text.insert('end',"Left Yaw\n")
		bebop.fly_direct(roll=0, pitch=0, yaw=-percentage, vertical_movement=0, duration=duration_s)
		bebop.flat_trim()

	elif (char == "e"):
		text.insert('end',"Right Yaw\n")
		drone.fly_direct(roll=0, pitch=0, yaw=percentage, vertical_movement=0, duration=duration_s)
		drone.flat_trim()
	else:
		drone.flat_trim()
		drone.smart_sleep(5)


  
