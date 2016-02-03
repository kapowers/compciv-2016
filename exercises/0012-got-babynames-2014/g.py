import os
import requests 
import string

babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")
zfile = open(babynames, 'w')
xfile = open(babynames, 'r')

print('letter         F       M')
print('------------------------')

#mydict = {'M': {}, 'F': {}} ##HOW DO YOU USE THIS NESTED ONE WITH THE BELOW CODE?
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

