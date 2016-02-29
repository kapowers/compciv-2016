import requests
from os import makedirs
PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)

URLS = #Code didn't save originally and can't find location of all 5 images I used. However,
#I would list URL of each image (not hyperlink) here 


for url in URLS:
    print("Downloading", url)
    resp = requests.get(url)
    fname = 
    print("Saving to", fname)
    with open(fname, 'wb') as w:
        w.write(resp.content)