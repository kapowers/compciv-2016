import os
import json

geocode_path = os.path.join('tempdata','mapzen','stanford.json')
geocode = open(geocode_path, 'r')
txt = geocode.read()
geocode.close()

mydict = json.loads(txt)
mykeys = mydict.keys()
mylist = list(mkeys)
myvals = mydict.values()
listvals = list(myvals)

#For each object within the Feature list
For x in mydict.values():
	mydict.get('label')
	mydict.get
#	find the label, confidence
# 	find the long and latitude within the coordinates object
