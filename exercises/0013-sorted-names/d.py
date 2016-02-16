import os
import requests 

url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
resp = requests.get(url)
babynames = os.path.join("tempdata","ssa_baby_names","ssa-babynames-nationwide-2014.txt")

x = 0
y = 0

x_list = []
f = open(babynames, 'r')
for line in f:
    name, sex, babies = line.strip().split(',')
    if 'x' in name:
        row = [name, sex, int(babies)]
        x_list.append(row)
	    if sex == 'F' and x < 5:
			if x == 0:
				print('Females')
			x += 1
			print("%d. %s %s" % (x,name,babies))
			if x == 5:
				print('')
		elif sex == 'M' and y < 5:
			if y == 0:
				print('Males')
			y += 1
			print("%d. %s %s" % (y,name,babies))