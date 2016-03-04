from os.path import join
import json
import csv
DATA_FOLDER = 'tempdata'
WRANGLED_CSV_FILE = join(DATA_FOLDER, 'wrangledbabynames.csv')
WRANGLED_JSON_FILE = join(DATA_FOLDER, 'wrangledbabynames.json')

with open(WRANGLED_CSV_FILE, 'r') as xfile:
	datarows = list(csv.DictReader(xfile))

for x in datarows:
	x['total'] = int(x['total'])
	x['males'] = int(x['males'])
	x['females'] = int(x['females'])
	x['ratio'] = int(x['ratio'])

anotherone = open(WRANGLED_JSON_FILE, 'w')
jsontext = json.dumps(datarows, indent =2)
anotherone.write(jsontext)
anotherone.close()

csvtxt = open(WRANGLED_CSV_FILE).read()
jsontxt = open(WRANGLED_JSON_FILE).read()
print("CSV has:", len(csvtxt), "characters")
print("JSON has:", len(jsontxt), "characters")
size_ratio = round(((len(jsontxt) - len(csvtxt)) / len(csvtxt)), 1)
print("JSON requires", size_ratio, "times more text characters than CSV")