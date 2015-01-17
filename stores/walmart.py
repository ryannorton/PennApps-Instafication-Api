
import requests
import json
from pprint import pprint

api_key = 'gqjsnjas9av755pcz8mek3ma'

class Walmart:
	
	def search(self, item):
		search = requests.get('http://api.walmartlabs.com/v1/search?apiKey=' + api_key + '&lsPublisherId=Postmates&query=' + item)
		data = json.loads(search.text)
		itemId = data['items'][0]['itemId']

		if itemId:
			lookup = requests.get('http://api.walmartlabs.com/v1/items/' + str(itemId) + '?apiKey=' + api_key + '&lsPublisherId=Postmates&format=json')
			data = json.loads(lookup.text)
			salePrice = data['salePrice']

			return {'item': item, 'price': salePrice, 'store': 'Walmart'}
		else:
			return None

walmart = Walmart()	
print walmart.search('Dyson DC40 Origin Upright Vacuum Cleaner')