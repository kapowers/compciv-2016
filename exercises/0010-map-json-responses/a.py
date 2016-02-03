import json
import requests
import os
if not os.path.exists('tempdata/googlemaps'):
	os.makedirs('tempdata/googlemaps')
if not os.path.exists('tempdata/mapzen'):
	os.makedirs('tempdata/mapzen')
from glob import glob

all_line_count = 0
all_characters = 0

mapzen_line_count = 0
mapzen_all_characters = 0

googlemaps_url = "http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json"
anotherone = "http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json"

resp = requests.get(googlemaps_url)
googlemaps_path = os.path.join("tempdata", "googlemaps", "stanford.json")
googlemaps_file = open(googlemaps_path, 'w')
googlemaps_file.write(resp.content)

googlemaps_file = open(googlemaps_path, 'r')
for line in googlemaps_file:
	all_line_count += 1
	all_characters += len(line)

googlemaps_file.close()
print("---")
print("Downloading from:", googlemaps_url)
print("Writing to:", googlemaps_path)
print("Wrote", all_line_count, "lines and", all_characters, "characters")
print("---")

resp = requests.get(anotherone)
mapzen_path = os.path.join("tempdata","mapzen","stanford.json")
mapzen_file = open(mapzen_path,'wb')
mapzen_file.write(resp.content)

mapzen_file = open(mapzen_path, 'r')
for line in mapzen_file:
	mapzen_line_count  += 1
	mapzen_all_characters += len(line)
mapzen_file.close()

print("Downloading from:", anotherone)
print("Writing to:", mapzen_path)
print("Wrote", mapzen_line_count, "lines and", mapzen_all_characters, "characters")




