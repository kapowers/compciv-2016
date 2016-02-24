import os
filename = os.path.join("tempdata","ssa-babynames-nationwide-2014.txt")

namesdict = {}
for line in open(filename,'r'):	
	name, sex, babies = line.strip().split(',')
	if namesdict.get(name):
		namesdict[name] += int(babies)
	else:
		namesdict[name] = int(babies)

myitems = namesdict.items()
mylist = list(myitems)

allbabies = 0
for you in mylist:
	allbabies += you[1]

def foo(x):
	return(x[1])

anotherlist = sorted(mylist, key=foo, reverse=True)
begin = 0
for baby in anotherlist[0:10]:
	begin += baby[1]
print("Names 1 to 10: ", round(begin * 100/allbabies, 1))
begin = 0
for baby in anotherlist[10:100]:
	begin += baby[1]
print("Names 11 to 100: ", round(begin * 100/allbabies,1))
begin = 0
for baby in anotherlist[100:1000]:
	begin += baby[1]
print("Names 101 to 1000: ",round(begin * 100/allbabies,1))
begin = 0
for baby in anotherlist[1000:10000]:
	begin += baby[1]
print("Names 1001 to 100000: ",round(begin * 100/allbabies,1))
begin = 0
for baby in anotherlist[10000:30579]:
	begin += baby[1]
print("Names 10001 to 30579: ",round(begin * 100/allbabies,1))