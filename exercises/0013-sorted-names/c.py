import requests
import os
if not os.path.exists('tempdata/ssa_baby_names'):
	os.makedirs('tempdata/ssa_baby_names')
from glob import glob

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")

namedict = {}

with open(babynames) as b:
	for line in b:
		name, sex, babies = line.strip().split(',')
		if namesdict.get(name):
			namesdict[name] += int(babies)
		else:
			namesdict[name] = int(babies)
	print(name,babies)
	#filter to include only key-value pairs in which value is at least 2,000
	#sort by length of name and # of babies
def namelength():
	return len(name)
sorted(babylist, key = namelength)
def babynumber():
	return babies
sorted(babylist), key = babynumber)
