import os
import requests 

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")
zfile = open(babynames, 'wb')
zfile.write(resp.content)

girls = 0
boys = 0

zfile = open(babynames, 'r')
for line in zfile:
	name, sex, babies = line.strip().split(',')
	if sex == 'F':
		girls += int(line.split(',')[2])
	else:
		boys += int(line.split(',')[2])
	

print('F: ',girls)
print('M: ',boys)