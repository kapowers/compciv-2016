import os
import json

geocode_path = os.path.join('tempdata','mapzen','stanford.json')
geocode = open(geocode_path, 'r')
txt = geocode.read()
geocode.close()

mydict = json.loads(txt)
features = mydict['features']

#features[1]['properties']

#For each object within the Feature list
for feature in features:
	mylist = []
	props = feature['properties']
	coords = feature['geometry']['coordinates']
	#print(props['label'], props['confidence']
	mylist.append(props['label'])
	mylist.append(str(props['confidence']))
	mylist.append(str(coords[0]))
	mylist.append(str(coords[1]))
	print(";".join(mylist))

