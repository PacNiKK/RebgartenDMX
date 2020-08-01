import array as ar
import time
from filehandler import load_scene
from ola.ClientWrapper import ClientWrapper

#path to scene files
path='scenes/'

universe=1
frame=50

#load yaml files into lists
sceneA=load_scene(path+'sceneA.yaml')
sceneB=load_scene(path+'sceneB.yaml')
sceneC=load_scene(path+'sceneC.yaml')
sceneD=load_scene(path+'sceneD.yaml')
sceneE=load_scene(path+'sceneE.yaml')

stage=sceneA
#scene_change(stage)

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
"""time.sleep(3)
scene_change(sceneB)
time.sleep(3)
scene_change(sceneC)
time.sleep(3)
scene_change(sceneD)
time.sleep(3)
scene_change(sceneE)"""

def scene_fade(scene,time):
	wrapper.AddEvent(time,wrapper.Stop)
	wrapper.Run()
	steps=time/frame
	delta=ar.array('f',[])
	send=ar.array('B',[])
	for i_channel in range(len(scene)):
		delta.append(scene[i_channel]-stage[i_channel])
		send.append(stage[i_channel])
	for i_time in range(steps):
		#calculate new frame
		for i_channel2 in range(len(stage)):
			send[i_channel2]=int(stage[i_channel2]+i_time*(delta[i_channel2]/steps))
		client.SendDmx(universe,send)
		print(i_time)
		print(i_time*(delta[i_channel2]/steps))
		print(send)
		time.sleep(time/steps/1000)
	scene_change(scene)
	
scene_fade(sceneA,10000)
scene_fade(sceneB,10000)
scene_fade(sceneC,10000)
scene_fade(sceneD,10000)
scene_fade(sceneE,10000)