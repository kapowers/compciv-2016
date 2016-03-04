from os.path import join, basename
from glob import glob
DATA_FOLDER = 'tempdata'
alltxtfiles_path = join(DATA_FOLDER, '*.txt')
alltxtfiles_names = glob(alltxtfiles_path)

tally = {'M': set(), 'F': set()}

for name in alltxtfiles_names:
	othername = basename(name)
	year = othername[3:7]
	if year >= "1950":
		for line in open(name, 'r'):
			name, gender, babies = line.split(',')
			tally[gender].add(name)

print("F:", len(tally['F']),
	  "M:", len(tally['M']))

f_to_m_ratio = round(100 * len(tally['F']) / len(tally['M']))
print("F/M baby ratio:", f_to_m_ratio)