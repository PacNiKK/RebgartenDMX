import array
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

print('load scene A: '+sceneA)
print('load scene B: '+sceneB)
print('load scene C: '+sceneC)
print('load scene D: '+sceneD)
print('load scene E: '+sceneE)


def DmxSent(state):
	wrapper.Stop()
	
#change to 'scene'
def scene_change(scene, time):
pass	
	

