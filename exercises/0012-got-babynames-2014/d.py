import os
import requests 

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")
zfile = open(babynames, 'wb')
zfile.write(resp.content)

x = 0
y = 0

zfile = open(babynames, 'r')

# traverse each line in file
for line in zfile:
	name, sex, babies = line.strip().split(',')
	if sex == 'F' and x < 5:
		if x == 0:
			print('Top baby girl names')
		x += 1
		print("%d. %s %s" % (x,name,babies))
		if x == 5:
			print('')
	elif sex == 'M' and y < 5:
		if y == 0:
			print('Top baby boy names')
		y += 1
		print("%d. %s %s" % (y,name,babies))


