#filehandler.py
import yaml
import array
import numpy as np

#imports a yaml list in 'path' and returns it as an array
def load_scene(path):
	array ('B',[])
	int i=0
	data.items()[0][1]
	with open(path) as f:
		data=yaml.load(f, Loader=yaml.FullLoader)
	list=data.items()[0][1]
	for channel in list:
		array[i]=channel
		i+=1
	return array