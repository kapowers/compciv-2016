import os
filename = os.path.join("tempdata","ssa-babynames-nationwide-2014.txt")

baby_list = []



for line in open(filename, 'r'):
	name, sex, babies = line.strip().split(',')
	row = [name, sex, int(babies)]
	baby_list.append(row)


def foo(row):
	return row[2]
	#return int(baby_list['babies']) #why is there an IndexError


sortybabies = sorted(baby_list, reverse = True, key = foo) 


x = 0
for row in sortybabies[0:10]:
	x += 1
	name = row[0]
	sex = row[1]
	babies =row[2]
	print("%d. %s, %s, %s" % (x,name, sex, babies))
		#how to delineate top 10 without gender (top 10 overall??)



