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
	client.SendDmx(universe,scene,DmxSent)
	wrapper.Run()
	

scene_change(sceneA)
time.sleep(3)
scene_change(sceneB)
time.sleep(3)
scene_change(sceneC)
time.sleep(3)
scene_change(sceneD)
time.sleep(3)
scene_change(sceneE)

def scene_fade(scene):
	delta=ar.array('B',[])
	i_channel=0
	for channel in scene:
		delta.append(scene[i_channel]-stage[i_channel])
		i+=1
	print(delta)
	
scene_fade(sceneA)
scene_fade(sceneB)
scene_fade(sceneC)
scene_fade(sceneD)
scene_fade(sceneE)