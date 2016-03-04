
import requests
from os import makedirs
from os.path import join
from shutil import unpack_archive
from glob import glob
SOURCE_URL = 'https://www.ssa.gov/oact/babynames/names.zip'
DATA_FOLDER = 'tempdata'
DATA_ZIP_PATH = join(DATA_FOLDER, 'names.zip')

makedirs(DATA_FOLDER, exist_ok=True)

print("Downloading", SOURCE_URL)
resp = requests.get(SOURCE_URL)
with open(DATA_ZIP_PATH, 'wb') as f:
    f.write(resp.content)

unpack_archive(DATA_ZIP_PATH, extract_dir=DATA_FOLDER)

babynamenames = glob(join(DATA_FOLDER, '*.txt'))
print("There are", len(babynamenames), 'txt files')