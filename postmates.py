import os
import requests
import json

class Postmates:

	BASE_URL = "https://api.postmates.com/v1/customers/"
	api_key = "850a408d-7644-43b0-990b-0adfbb505b9c"
	test_id = "cus_KAbkx0F1UjLZaV"

	def quote(self, pickup, dropoff):
		url = self.BASE_URL + self.test_id + "/delivery_quotes"
		params = {
			"pickup_address" : pickup,
			"dropoff_address" : dropoff
		}
		return json.dumps(requests.post(url, data=params, auth=(self.api_key, '')).text)

	def list(self):
		url = self.BASE_URL + self.test_id + "/deliveries"	
		return json.dumps(requests.get(url, auth=(self.api_key, '')).text)

	def create(self, quote, manifest, pickup_name, pickup_phone_number, dropoff_name, dropoff_address, dropoff_phone_number):
		url = self.BASE_URL + self.test_id + "/deliveries"
		params = {
			"manifest" : manifest,
			"pickup_name" : pickup_name,
			"pickup_address" : pickup_address,
			"pickup_phone_number" : pickup_phone_number,
			"dropoff_name" : dropoff_name,
			"dropoff_address" : dropoff_address,
			"dropoff_phone_number" : dropoff_phone_number,
			"quote_id" : quote
		}

		return json.dumps(requests.post(url, data=params, auth=(self.api_key, '')).text)

	def poll(self, delivery):
		url = self.BASE_URL + self.test_id + "/deliveries/" + delivery
		return json.dumps(requests.get(url, auth=(self.api_key, '')).text)

x = Postmates()
print x.poll('del_KAe81Ndj9kZulk')
