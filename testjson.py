import requests
import json

url = "http://x.x.x.x:60175/inventory/deviceinfo?loid=raisecom0414"

payload = {}
headers = {
  'Authorization': 'Basic YWRtaW5pc3RyYXRvcjpyYWlzZWNvbQ=='
}

response = requests.request("GET", url, headers=headers, data = payload)
response.encoding='utf-8'

result=response.text

print(result)

r=json.loads(result)['data']
print(r)

print(r[0]['ip'])
ip=r[0]['ip']
