import requests

url = 'http://vudu.com'
payload = '//google.com'

r = requests.get(url, payload, timeout=1)

print(r.url,"\n")

print(r.headers, "\n")
print(r.status_code, "\n")

