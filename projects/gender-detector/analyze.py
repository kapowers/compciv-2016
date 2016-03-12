from os.path import join
import csv
from gender import detect_gender
DATA_DIR = 'tempdata'
CLASSIFIED_DATA_FILENAME = join(DATA_DIR, 'classified_data.csv')

MIN_GENDER_RATIO = 95
NAMES_DATA_ROWS = list(csv.DictReader(open(CLASSIFIED_DATA_FILENAME)))

for d in NAMES_DATA_ROWS:
	if d['ratio']:
		d['ratio'] = int(d['ratio'])

print('Gender tally:')
all_genders = {'M': 0, 'F': 0}
for d in NAMES_DATA_ROWS:
	if d['ratio'] and d['ratio'] >= MIN_GENDER_RATIO:
		all_genders[d['gender']] += 1

print("Total Female Guests:", all_genders['F'])
print("Total Male Guests:", all_genders['M'])
rftotal = round(100 * all_genders['F'] / (all_genders['F'] + all_genders['M']))
rmtotal = round(100 * all_genders['M'] / (all_genders['M'] + all_genders['F']))
print('Female ratio of the total:', str(rftotal) + '%')
print('Male ratio of the total:', str(rmtotal) + '%')

print("-------------------------------")

year_break = {'M': 0, 'F': 0}
year_new = {'M': 0, 'F': 0}
for d in NAMES_DATA_ROWS:
	if d['ratio'] and d['ratio'] >= MIN_GENDER_RATIO:
		if d['year'] == '2015':
			year_break[d['gender']] += 1
		elif d['year'] == '2016':
			year_new[d['gender']] +=1

print('Female Guests in 2015:', year_break['F'])
print('Female Guests in 2016:', year_new['F'])

print("-------------------------------")

year_old = {'M': 0, 'F': 0}

for d in NAMES_DATA_ROWS:
	if d['ratio'] and d['ratio'] >= MIN_GENDER_RATIO:
		if d['year'] == '2015':
			year_old[d['gender']] += 1

print("Men in the Year 2015:", year_old['M'])
print('Ratio of men in 2015 to all women ever:', year_old['M'], '/' ,all_genders['F'])
print("CONCLUSION: Trevor Noah needs more female guests NOW!!")