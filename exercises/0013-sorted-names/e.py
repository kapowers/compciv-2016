import os
import requests 

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")

zfile = open(babynames, 'r')

for line in zfile:
	name, sex, babies = line.strip().split(',')