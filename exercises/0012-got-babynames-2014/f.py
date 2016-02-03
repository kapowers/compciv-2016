import os
import requests 
import string

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")
zfile = open(babynames, 'wb')
zfile.write(resp.content)
xfile = open(babynames, 'r')

mydict = {} 

for line in xfile:
	name, sex, babies = line.strip().split(',')
	last_letter = name[-1] 
	if mydict.get(last_letter):
		mydict[last_letter] += int(babies)
	else:
		mydict[last_letter] = int(babies) 
for key in string.ascii_lowercase:
	val = mydict[key]
	print(key,':',val)

