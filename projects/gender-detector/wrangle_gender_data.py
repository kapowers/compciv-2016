from os.path import join, basename
import csv
DATA_FOLDER = 'tempdata'

WRANGLED_HEAD = ['name', 'gender', 'ratio', 'females', 'males', 'total']
WRANGLED_DATA_FILE = join(DATA_FOLDER, 'wrangledbabynames.csv')
START_YEAR = 1950
END_YEAR = 2014

years = list(range(START_YEAR, END_YEAR, 10))
years.append(END_YEAR)

namedict = {}
for year in years:
	filename = join(DATA_FOLDER, 'yob' + str(year) + '.txt')
	print("Parsing", filename)
	with open(filename, 'r') as thatfile:
		for line in thatfile:
			name, gender, count = line.split(',')
			if not namedict.get(name):
				namedict[name] = {'F': 0, 'M': 0}
			namedict[name][gender] += int(count)

bad_ass_list = []
for name, babiescount in namedict.items():
	xdict = {'name': name, 'females': babiescount['F'], 'males': babiescount['M']}
	xdict['total'] = xdict['males'] + xdict['females']
	if xdict['females'] >= xdict['males']:
		xdict['gender'] = 'F'
		xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
	else:
		xdict['gender'] = 'M'
		xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])
	bad_ass_list.append(xdict)

yofile = open(WRANGLED_DATA_FILE, 'w')
yocsv = csv.DictWriter(yofile, fieldnames=WRANGLED_HEAD)
yocsv.writeheader()

def order(xdict):
	return(-xdict['total'],xdict['name'])

for row in sorted(bad_ass_list, key = order):
	yocsv.writerow(row)

yofile.close()

with open(WRANGLED_DATA_FILE, 'r') as t:
	for line in t.readlines()[0:5]:
		print(line.strip())