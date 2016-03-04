from os.path import join, basename
import csv
DATA_FOLDER = 'tempdata'
YEAR = 2014
filename = join (DATA_FOLDER, 'yob' + str(YEAR) + '.txt')

WRANGLED_HEADS = ['year','name', 'gender', 'ratio', 'females', 'males', 'total']
WRANGLED_DATA_FILE = join(DATA_FOLDER, 'wrangled2014.csv')

namesdict = {}
with open(filename, 'r') as thatfile:
	for line in thatfile:
		name, gender, count = line.split(',')
		if not namesdict.get(name):
			namesdict[name] = {'M': 0, 'F': 0}
		namesdict[name][gender] += int(count)

bad_ass_list = []
for name, babiescount in namesdict.items():
	xdict = {}
	xdict['year'] = YEAR
	xdict['name'] = name
	xdict['females'] = babiescount['F']
	xdict['males'] = babiescount['M']
	xdict['total'] = xdict['males'] + xdict['females']
	if xdict['females'] >= xdict['males']:
		xdict['gender'] = 'F'
		xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
	else:
		xdict['gender'] = 'M'
		xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])

	bad_ass_list.append(xdict)

newfile = open(WRANGLED_DATA_FILE, 'w')
ncsv = csv.DictWriter(newfile, fieldnames = WRANGLED_HEADS)
ncsv.writeheader()

def greatest(xdict):
	return(-xdict['total'],xdict['name'])

my_final_list = sorted(bad_ass_list, key = greatest)

for row in my_final_list:
	ncsv.writerow(row)
newfile.close()

finalfile = open(WRANGLED_DATA_FILE, 'r')
finallines = finalfile.readlines()[0:5]
for line in finallines:
	print(line.strip())