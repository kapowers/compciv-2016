import requests
from os import makedirs
from os.path import join
from shutil import unpack_archive
from glob import glob
SOURCE_URL = 'https://raw.githubusercontent.com/kapowers/compciv-2016/master/projects/gender-detector/Stash/Trevor%20Noah%20Guests.csv'
DATA_DIR = 'tempdata'
DATA_PATH = join(DATA_DIR, 'names.csv')
makedirs(DATA_DIR, exist_ok=True)

print("Downloading", SOURCE_URL)
resp = requests.get(SOURCE_URL)
with open(DATA_PATH, 'wb') as f:
    f.write(resp.content)


