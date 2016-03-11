from os.path import join
import json
WRANGLED_DIR = 'tempdata/wrangled'
WRANGLED_CSV_FILENAME = join(WRANGLED_DIR, 'wranglednames.csv')
NAMES_DATA_ROWS = open(WRANGLED_CSV_FILENAME)

def detect_gender(name):
    result = { 'name': name, 'gender': None, 'ratio': None, 'males': 0, 'females': 0, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        if name.lower() == row['name'].lower():
            result = row
            break
    return result