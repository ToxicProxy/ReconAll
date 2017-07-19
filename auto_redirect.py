import requests

payload = '//google.com'
url = 'http://vudu.com' + payload

r = requests.get(url, timeout=1)

print("URL:", r.url,"\n")

print("Headers:", r.headers, "\n")
print("Status:", r.status_code, "\n")

