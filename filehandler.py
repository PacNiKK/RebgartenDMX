import yaml
def load_scene(path):
	with open(path) as f:
		data=yaml.load(f, Loader=yaml.FullLoader)
		return data.items()[0][1]


