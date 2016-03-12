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

print("F:", all_genders['F'])
print("M:", all_genders['M'])
rftotal = round(100 * all_genders['F'] / (all_genders['F'] + all_genders['M']))
rmtotal = round(100 * all_genders['M'] / (all_genders['M'] + all_genders['F']))
print('Female ratio of the total:', str(rftotal) + '%')
print('Male ratio of the total:', str(rmtotal) + '%')

#3 ways to analyze your dataset by gender
#ratio of men to women, ratio by year, what is the third?