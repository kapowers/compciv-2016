from os.path import join, basename
from glob import glob
DATA_FOLDER = 'tempdata'
alltxtfiles_path = join(DATA_FOLDER, '*.txt')
alltxtfiles_names = glob(alltxtfiles_path)

myfilenames = []
for name in alltxtfiles_names:
	othername = basename(name)
	year = othername[3:7]
	if year >= "1950":
		myfilenames.append(name)
totaldict = {'M': 0, 'F': 0}

for name in myfilenames:
	babyfile = open(name, "r")
	for line in babyfile:
		name, gender, babies = line.split(',')
		totaldict[gender] += int(babies)

print("F:", str(totaldict['F']).rjust(6),
	  "M:", str(totaldict['M']).rjust(6))

f_to_m_ratio = round(100 * totaldict['F'] / totaldict['M'])
print("F/M baby ratio:", f_to_m_ratio)