from os.path import join
import json
DATA_FOLDER = 'tempdata'
WRANGLED_JSON_FILENAME = join(DATA_FOLDER, 'wrangledbabynames.json')
NAMES_DATA_ROWS = json.load(open(WRANGLED_JSON_FILENAME))

def detect_gender(name):
	result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': 0, 'females': 0, 'total': 0}
	for row in NAMES_DATA_ROWS:
		if name.lower() == row['name'].lower():
			result = row
			break
	return result