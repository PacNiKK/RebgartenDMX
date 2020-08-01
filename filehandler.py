#filehandler.py
import yaml
import array as ar
import numpy as np

#imports a yaml list in 'path' and returns it as an array
def load_scene(path):
	array=ar.array ('B',[])
	i=0
	with open(path) as f:
		data=yaml.load(f, Loader=yaml.FullLoader)
	list=data.items()[0][1]
	for channel in list:
		array.append(channel)
		i+=1
	return array