import os
filename = os.path.join("tempdata","ssa-babynames-nationwide-2014.txt")

namesdict = {}

for line in open(filename, 'r'):
	name, sex, babies = line.strip().split(',')
	if namesdict.get(name):
		namesdict[name] += int(babies)
	else:
		namesdict[name] = int(babies)

items = namesdict.items()
mylist = list(items)
popular_names_list = [] 

for key, val in items:
	if val > 1999 and key not in popular_names_list:
		num = val
		popular_names_list.append([key, val])
	if key in popular_names_list:
		num = int(val) + int(popular_names_list[1])
		popular_names_list.append([key,num])

def foo(x):
	return (len(x[0]), x[1])

anotherone = sorted(popular_names_list, key = foo, reverse=True)
again = anotherone[0:10]

for baby in again:
	print(baby[0].ljust(10), str(baby[1]).rjust(10))
