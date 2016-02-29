import requests
from os import makedirs
PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)

URLS = 

for url in URLS:
    print("Downloading", url)
    resp = requests.get(url)
    fname = 
    print("Saving to", fname)
    with open(fname, 'wb') as w:
        w.write(resp.content)