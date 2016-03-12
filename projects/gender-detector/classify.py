from os.path import join, basename
import csv
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'tempdata'
WRANGLED_DIR = 'tempdata/wrangled'
WRANGLED_DATA_PATH = join(WRANGLED_DIR, 'wranglednames.csv')
CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified_data.csv')

def extractable_usable_name(name):
	return name.split(' ')[0]

classified_headers = ['year', 'name', 'description', 'usable_name', 'gender', 'ratio']

w = open(CLASSIFIED_DATA_FILENAME, 'w')
dw = DictWriter(w, fieldnames=classified_headers)
dw.writeheader()

with open(WRANGLED_DATA_PATH) as r:
	datarows = list(DictReader(r))
	ct = 0
	for row in datarows:
		usable_name = extractable_usable_name(row['name'])
		ct += 1
		print("Row:", ct, "extracting --", usable_name, "--from", row['name'])
		gender_result = detect_gender(usable_name)
		row['usable_name'] = usable_name
		row['gender'] = gender_result['gender']
		row['ratio'] = gender_result['ratio']
		dw.writerow(row)