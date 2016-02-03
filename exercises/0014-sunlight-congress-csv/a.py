import requests
import os
if not os.path.exists('tempdata/sunlight-legislators'):
	os.makedirs('tempdata/sunlight-legislators')
from glob import glob

url = "http://stash.compciv.org/congress/2016-01/sunlight-legislators.csv"
resp = requests.get(url)
sunlightlegislators = os.path.join("tempdata","sunlight-legislators.csv")
zfile = open(sunlightlegislators, 'w')
zfile.write(resp.text)

all_line_count = 0

zfile = open(sunlightlegislators,'r')
for x in zfile:
	all_line_count += 1
zfile.close()

print("There are",all_line_count,"lines in",sunlightlegislators)