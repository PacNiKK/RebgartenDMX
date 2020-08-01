import yaml
with open('scenes/sceneA.yaml') as f:

	data=yaml.load(f,Loader=yaml.FullLoader)
	print(data)


