from os.path import join, basename
year = 2014
DATA_FOLDER = 'tempdata'
filename = join(DATA_FOLDER, 'yob' + str(year) + '.txt')

names_dict = {}
thatfile = open(filename, 'r')
for line in thatfile:
	name, gender, count = line.split(',')
	if not names_dict.get(name):
		names_dict[name] = {'M': 0, 'F': 0}
	names_dict[name][gender] += int(count)
thatfile.close()

total_names = len(names_dict.keys())

total_babes = 0
for b in names_dict.values():
	babes = b['M'] + b['F']
	total_babes += babes

print("Total:", total_names, 'unique names for', total_babes, 'babies')

for gender in ['M', 'F']:
	ncount = 0
	bcount = 0
	for b in names_dict.values():
		if b[gender] > 0:
			bcount += b[gender]
			ncount += 1
	print("   %s:" % gender, ncount, "unique names for", bcount, "babies")
