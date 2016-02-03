import os
import json

geocode_path = os.path.join('tempdata','mapzen','stanford.json')
geocode = open(geocode_path, 'r')
txt = geocode.read()
geocode.close()

mydict = json.loads(txt)

xlist = []
x = mydict['geocoding']
y = x['query']
xlist.append('type: '+ mydict['type'])
xlist.append('text: '+ y['text'])
xlist.append('size: '+str(y['size']))
xlist.append('boundary.country: '+y['boundary.country'])
print("\n".join(str(x) for x in xlist))

