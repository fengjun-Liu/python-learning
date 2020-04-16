import unittest
import requests
import json

class TestRequestsMethods(unittest.TestCase):

	def test_ip(self):
		url = "http://172.16.110.56:60175/inventory/deviceinfo?loid=raisecom0414"

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
		self.assertEqual(ip,'10.0.51.84')
		
if __name__=='__main__':
	unittest.main()
