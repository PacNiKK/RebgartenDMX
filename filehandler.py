#filehandler.py
import yaml

#imports a yaml list in 'path' and returns it as a list
def load_scene(path):
	with open(path) as f:
		data=yaml.load(f, Loader=yaml.FullLoader)
	return data.items()[0][1]