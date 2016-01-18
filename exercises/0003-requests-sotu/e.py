import requests
requests.get("https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address")
resp = requests.get("https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address")
a = resp.text
a.count('Applause')
print(a.count('Applause'))
a.lower().count("applause")
print(a.lower().count("applause"))
a.count('<p>')
print(a.count('<p>'))
