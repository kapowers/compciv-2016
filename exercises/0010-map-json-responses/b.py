import os
import json

geocode_path = os.path.join('tempdata','googlemaps','stanford.json')
geocode = open(geocode_path, 'r')
txt = geocode.read()
geocode.close()

mydict = json.loads(txt)
print(mydict['status'])




