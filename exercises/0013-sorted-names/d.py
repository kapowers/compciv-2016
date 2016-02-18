import os
filename = os.path.join("tempdata","ssa-babynames-nationwide-2014.txt")

x = 0
y = 0

x_girl = []
y_boy = []

for line in open(filename,'r'):	
    name, sex, babies = line.strip().split(',')
    if 'x' in name.lower() and sex == 'F':
        row = [name, sex, int(babies)]
        x_girl.append(row)
print('Female')
for girl in x_girl:
	if int(girl[2]) > 1588:
		x += 1
		name = girl[0]
		babies = girl[2]
		print("%d. %s             %s" % (x,name.ljust(11),babies))

for line in open(filename,'r'):	
    name, sex, babies = line.strip().split(',')
    if 'x' in name.lower() and sex == 'M':
        row = [name, sex, int(babies)]
        y_boy.append(row)
print('Male')
for dude in y_boy:
	if int(dude[2]) > 3702:
		y += 1
		dudename = dude[0]
		dudebabies = dude [2]
		print("%d. %s            %s" % (y,dudename.ljust(11),dudebabies))
