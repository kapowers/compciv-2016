from os.path import join
import csv
DATA_FOLDER = 'tempdata'
WRANGLED_DATA_FILE = join(DATA_FOLDER, 'wrangled2014.csv')

newfile = open(WRANGLED_DATA_FILE, 'r')
datarows = list(csv.DictReader(newfile))

for r in datarows:
	r['total'] = int(r['total'])
	r['males'] = int(r['males'])
	r['females'] = int(r['females'])
	r['ratio'] = int(r['ratio'])

bigdatarows = []
for row in datarows:
	if int(row['total']) >= 100:
		bigdatarows.append(row)

print("Popular names with a gender ratio bias of less than or equal to:")
for genderratio in (60,70,80,90,99):
	
	filteredrows = []
	for row in bigdatarows:
		if row['ratio'] <= genderratio:
			filteredrows.append(row)

	print(genderratio,"%: ", len(filteredrows), "/", len(bigdatarows))