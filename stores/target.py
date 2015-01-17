import requests
import json
from bs4 import BeautifulSoup

class Target:

	name = "Target"
	BASE_URL = "http://www.target.com/s?searchTerm="

	def search(self, item):
		url = self.BASE_URL + item
		try:
			results = BeautifulSoup(requests.get(url).text).find_all('p', class_='price-label')[0].text.strip()[1:]
			return float(results)
		except:
			return None
