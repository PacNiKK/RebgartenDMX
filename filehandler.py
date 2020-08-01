#filehandler.py
import yaml
import array

#imports a yaml list in 'path' and returns it as an array
def load_scene(path):
	
	with open(path) as f:
		data=yaml.load(f, Loader=yaml.FullLoader)
		
		return_list=';'.join(data.items()[0][1])
		return_array = []
		for item in return_list.split(';'):
			return_array.append(item)
	return return_array
	
	