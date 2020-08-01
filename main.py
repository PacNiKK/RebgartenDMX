import array as ar
import time
from filehandler import load_scene
from ola.ClientWrapper import ClientWrapper
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#path to scene files
path='scenes/'

universe=1
frame=50
fade=3000

#load yaml files into lists
sceneA=load_scene(path+'sceneA.yaml')
sceneB=load_scene(path+'sceneB.yaml')
sceneC=load_scene(path+'sceneC.yaml')
sceneD=load_scene(path+'sceneD.yaml')
sceneE=load_scene(path+'sceneE.yaml')
stage=sceneA

print(sceneA)
print(sceneB)
print(sceneC)
print(sceneD)
print(sceneE)

wrapper=ClientWrapper()
client=wrapper.Client()

def DmxSent(state):
	wrapper.Stop()
	
#change to 'scene'
def scene_change(scene):
	global stage
	client.SendDmx(universe,scene,DmxSent)
	wrapper.Run()
	stage=scene
	
scene_change(sceneA)

def scene_fade(scene,fade_time):
	steps=fade_time/frame
	delta=ar.array('f',[])
	send=ar.array('B',[])
	for i_channel in range(len(scene)):
		delta.append(scene[i_channel]-stage[i_channel])
		send.append(stage[i_channel])
	for i_time in range(steps):
		#calculate new frame
		for i_channel2 in range(len(stage)):
			send[i_channel2]=int(stage[i_channel2]+i_time*(delta[i_channel2]/steps))
		client.SendDmx(universe,send, DmxSent)
		print(send)
		time.sleep(float(fade_time)/float(steps)/1000)
	wrapper.Run()
	scene_change(scene)
	

def button_callback1(channel):
	print("fade to A")
	scene_fade(sceneA,fade)
def button_callback2(channel):
	print("fade to B")
	scene_fade(sceneB,fade)
def button_callback3(channel):
	print("fade to C")
	scene_fade(sceneC,fade)
def button_callback4(channel):
	print("fade to D")
	scene_fade(sceneD,fade)
def button_callback5(channel):
	print("fade to E")
	scene_fade(sceneE,fade)
		
GPIO.add_event_detect(3,GPIO.RISING,callback=button_callback1,bouncetime=250) # Setup event on pin 3 rising edge
GPIO.add_event_detect(5,GPIO.RISING,callback=button_callback2,bouncetime=250)
GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback3,bouncetime=250)
GPIO.add_event_detect(11,GPIO.RISING,callback=button_callback4,bouncetime=250)
GPIO.add_event_detect(13,GPIO.RISING,callback=button_callback5,bouncetime=250)
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up