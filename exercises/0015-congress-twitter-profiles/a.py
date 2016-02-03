import requests
import os
if not os.path.exists('tempdata/congress-twitter-profiles'):
	os.makedirs('tempdata/congress-twitter-profiles')
from glob import glob

url = "http://stash.compciv.org/congress-twitter/2016-01/congress-twitter-profiles.json"
resp = requests.get(url)
twitterprofiles = os.path.join("tempdata","congress-twitter-profiles.json")
zfile = open(twitterprofiles, 'w')
zfile.write(resp.text)

all_line_count = 0

zfile = open(twitterprofiles,'r')
for x in zfile:
	all_line_count += 1
zfile.close()

print("There are",all_line_count,"lines in",twitterprofiles)