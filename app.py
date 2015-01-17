from flask import Flask
import json
from stores.target import Target
from stores.walmart import Walmart

# Global Stores
target = Target()
walmart = Walmart()
STORES = [target, walmart]

app = Flask(__name__)
app.debug = True

def get(query):
	price = None
	name = None
	for store in STORES:
		result = store.search(query)
		if result and result < price or result and not price:
			price = result
			name = store.name
	return (name, price)

@app.route("/")
def home():
	return "PennApps bitch"

@app.route("/search/<item>")
def search(item):
	name, price = get(item)
	result = {
		'item' : item,
		'store' : name,
		'price' : price
	}
	return json.dumps(result)

if __name__ == "__main__":
    app.run()













