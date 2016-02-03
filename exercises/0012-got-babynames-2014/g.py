import os
import requests 
import string

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")
zfile = open(babynames, 'w')
zfile.write(resp.text)
xfile = open(babynames, 'r')

print('letter         F       M')
print('------------------------')

ydict = {}
xdict = {}

for line in xfile:
	name, sex, babies = line.strip().split(',')
	if sex == 'M':
		last_letter = name[-1]
		if ydict.get(last_letter):
			ydict[last_letter] += int(babies)
		else:
			ydict[last_letter] = int(babies)
	if sex == 'F':
		last_letter = name[-1]
		if xdict.get(last_letter):
			xdict[last_letter] += int(babies)
		else:
			xdict[last_letter] = int(babies)

for key in string.ascii_lowercase:
	xs = str(xdict[key])
	ys = str(ydict[key])
	print(key.ljust(7),xs.rjust(8),ys.rjust(7))

