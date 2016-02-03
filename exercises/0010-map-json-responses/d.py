import os
import json

geocode_path = os.path.join('tempdata','googlemaps','stanford.json')
geocode = open(geocode_path, 'r')
txt = geocode.read()
geocode.close()

mydict = json.loads(txt)

for x in mydict['results']:
	addresscomp =  x['address_components']

xlist = []
for r in addresscomp:
	xlist.append(r['long_name'])
print(";".join(xlist))




