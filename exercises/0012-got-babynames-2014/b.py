import os
import requests 

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")
zfile = open(babynames, 'wb')
zfile.write(resp.content)

babies = 0

zfile = open(babynames, 'r')
for line in zfile:
	babies += int(line.split(',')[2])

print("There are", babies ,"babies whose names were recorded in 2014.")