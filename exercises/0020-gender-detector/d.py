from os.path import join, basename
from glob import glob
DATA_FOLDER = 'tempdata'
alltxtfiles_path = join(DATA_FOLDER, '*.txt')
alltxtfiles_names = glob(alltxtfiles_path)

for name in alltxtfiles_names:
	tally = {'M': set(), 'F': set()}
	othername = basename(name)
	year = othername[3:7]
	if int(year) >= 1950:
		for line in open(name, 'r'):
			name, gender, babies = line.split(',')
			tally[gender].add(name)
		print(year)
		print("F:", len(tally['F']),
	  	"M:", len(tally['M']))
		f_to_m_ratio = round(100 * len(tally['F']) / len(tally['M']))
		print("F/M baby ratio:", f_to_m_ratio)