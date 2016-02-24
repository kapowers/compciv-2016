import requests
import json

def fetch_mapzen_response(location):
  """
  'location' is a string to be passed onto Mapzen API
  returns text string contained JSON-formatted data from Mapzen
  """
  mykey = read_mapzen_credentials()
  my_params = {'text': location, 'api_key': mykey}
  url = 'https://search.mapzen.com/v1/search'
  resp = requests.get(url, params = my_params)
  return resp.text

def parse_mapzen_response(txt):
  """
  'txt' is a string containing JSON-formatted text from Mapzen API
  returns dic containing useful key/values from most relevant result
  """
  gdict = {}
  stuff = json.loads(txt)
  if stuff['features']:
     gdict['status'] = 'OK'
     feature = stuff['features'][0]
     prop = feature['properties']
     gdict['confidence'] = prop['confidence']
     gdict['label'] = prop['label']

     coordinate = feature['geometry']['coordinates']
     gdict['longitude'] = coordinate[0]
     gdict['latitude'] = coordinate[1]
  else:
      gdict['status'] = None
  return gdict

def read_mapzen_credentials():
  creds_filename = "creds_mapzen.txt"
  keytxt = open(creds_filename).read().strip()
  return keytxt

def geocode(location):
    """
    Attempt to geocode a location string using Mapzen Search API.

    What it expects:
    -----------------
    It expects 'location' to be a string, 
    repping a human-readable geo location such as "Boston, MA"

    It also expects the variable 'CREDS_FILE' to point out existing file that contains
    a valid Mapzen Search key.

    What the function does:
    -----------------
    It opens and reads the file at CREDS_FILE to get the API Key.

    It calls the Mapzen Search API via a HTTP request, using the API Key, and the user-given 
    'location' string as the 'text' parameter.

    It deserializes the Mapzen Search response into a dictionary, using the JSON library.

    It then creates a dicitonary.


    What it returns:
    -----------------
    A dictionary containing these key-value pairs:

    -query_text: the 'location' string given by the user-given
    -label: The string label that Mapzen so generously provides in describing found location
    -confidence: A float repping the confidence value that Mapzen has in results.
    -latitude: a float representating the latitude coordinate
    -longitude: a float representating the longitude coordinate
    -status: "OK," a string that indicates a result was found. Else, None

    """
    raw = fetch_mapzen_response(location)
    mydict = parse_mapzen_response(raw)
    mydict['status'] = 'OK'
    mydict['query_string'] = location
    return mydict


  