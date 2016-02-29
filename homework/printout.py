from os.path import join, basename
from glob import glob
import json
PICS_DIR = 'pics'
RECOG_DIR = 'responses'

HTML_FILENAME = 'printout.html'
htmlfile = open(HTML_FILENAME, 'w')
htmlfile.write("<html><title>Whatsup Watson</title><body>")
htmlfile.write("<h1>Analysis by Kristen Powers</h1>")

for jsonname in glob(join(RECOG_DIR, '*.json')):
    print("Extracting", jsonname)
    j = json.load(open(jsonname))
    img = j['images'][0]
    imgname = img['image']
    htmlfile.write("<h2>%s</h2>" % imgname)

    imgfilename = join(PICS_DIR, imgname)

    htmlfile.write('<img src="%s">' % imgfilename)

htmlfile.close()