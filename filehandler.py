#filehandler.py
import yaml
import array
from numpy import array

#imports a yaml list in 'path' and returns it as an array
def load_scene(path):
	with open(path) as f:
		data=yaml.load(f, Loader=yaml.FullLoader)
	return array(data.items()[0][1])