import requests
requests.get("http://www.example.com")
resp = requests.get("http://www.example.com")
print(resp.status_code)
len(resp.text)
print(len(resp.text))
print(resp.url)