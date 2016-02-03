import requests
import os
if not os.path.exists('tempdata/ssa_baby_names'):
	os.makedirs('tempdata/ssa_baby_names')
from glob import glob

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")
zfile = open(babynames, 'wb')
zfile.write(resp.content)

all_line_count = 0

zfile = open(babynames,'r')
for x in zfile:
	all_line_count += 1
zfile.close()

print("There are",all_line_count,"lines in",babynames)


