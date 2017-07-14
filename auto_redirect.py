import requests

payload = '//google.com'

r = requests.get('https://vudu.com/', payload)
print(r.url)

