import requests
from os import makedirs
PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)

URLS = {'https://farm2.staticflickr.com/1638/24902500570_25c1894293_z_d.jpg', 'https://farm2.staticflickr.com/1467/23941893710_937ac8952a_z_d.jpg', 'https://farm2.staticflickr.com/1692/23609238704_70b48736d7_z_d.jpg' , 'https://farm2.staticflickr.com/1659/23869644609_6b02d41866_z_d.jpg','https://farm2.staticflickr.com/1632/23610659283_fa9936f7d7_z_d.jpg','https://farm2.staticflickr.com/1720/24237481605_8761572254_z_d.jpg'}

for url in URLS:
    print("Downloading", url)
    resp = requests.get(url)
    fname = 'pics'
    print("Saving to", fname)
    with open(fname, 'wb') as w:
        w.write(resp.content)