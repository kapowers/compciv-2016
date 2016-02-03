import os
import json

geocode_path = os.path.join('tempdata','googlemaps','stanford.json')
geocode = open(geocode_path, 'r')
txt = geocode.read()
geocode.close()

mydict = json.loads(txt)
for x in mydict['results']:
	xlist = []
	xlist.append(x['formatted_address'])
	xlist.append(x['geometry']['location']['lng'])
	xlist.append(x['geometry']['location']['lat'])
	print(";".join(str(x) for x in xlist))

