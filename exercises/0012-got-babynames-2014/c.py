import os
import requests 

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")
zfile = open(babynames, 'wb')
zfile.write(resp.content)

D = 0
K = 0

zfile = open(babynames, 'r')
for line in zfile:
	name, sex, babies = line.strip().split(',')
	if sex == 'F':
		if name == 'Daenerys':
			D += int(babies)
		elif "Khalees" in name:
			K += int(babies)
		elif "Khaless" in line:
			K += int(babies)

print('Daenerys:', D)
print('Khaeesi:', K)
