import array
import time
from filehandler import load_scene
from ola.ClientWrapper import ClientWrapper

#path to scene files
path='scenes/'

universe=1

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
	client.SendDmx(universe,[255,255,255],DmxSent)
	print(scene)
	wrapper.Run()
	

scene_change(sceneA)
time.sleep(1)
scene_change(sceneB)
time.sleep(1)
scene_change(sceneC)
time.sleep(1)
scene_change(sceneD)
time.sleep(1)
scene_change(sceneE)