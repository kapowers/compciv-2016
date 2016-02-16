import requests
import os
os.makedirs('tempdata', exist_ok=True)
url = "http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"
filename = 'tempdata/ssa-babynames-nationwide-2014.txt'

resp = requests.get(url)
txt = resp.text

zfile = open(filename, 'w')
zfile.write(txt)
zfile.close()


print('There are', len(txt) ,'characters in', filename)