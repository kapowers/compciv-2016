from os.path import join, basename
import requests
from os import makedirs
import csv
from csv import DictReader, DictWriter

DATA_DIR = 'tempdata'
DATA_PATH = join(DATA_DIR, 'names.csv')
WRANGLED_DIR = 'tempdata/wrangled'
WRANGLED_HEAD = ['year', 'name', 'description']
WRANGLED_DATA_PATH = join(WRANGLED_DIR, 'wranglednames.csv')

with open(DATA_PATH, 'r', encoding='latin1') as thatfile:
	for line in thatfile:
		year, name, description = line.split(',', 2)
		datarows = list(csv.DictReader(thatfile))

yofile = open(WRANGLED_DATA_PATH, 'w')
yocsv = DictWriter(yofile, fieldnames=WRANGLED_HEAD)
yocsv.writeheader()

mylist = []
for year, name, description in datarows:
	xdict = {'year': year, 'name': name, 'description': description}
	mylist.append(xdict)

for row in mylist:
	yocsv.writerow(row)
yofile.close()







