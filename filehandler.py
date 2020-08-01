#filehandler.py
import yaml
import array
import numpy as np

#imports a yaml list in 'path' and returns it as an array
def load_scene(path):
	with open(path) as f:
		data=yaml.load(f, Loader=yaml.FullLoader)
	return np.asarray(data.items()[0][1],dtype=np.int)