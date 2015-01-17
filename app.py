from flask import Flask
import json

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
	return "PennApps bitch"

@app.route("/search")
def search(item):
	result = {
		'item' : 'Baseball'
		'store' : 'Walmart',
		'price' : 35.62
	}
	return json.dumps(result)

if __name__ == "__main__":
    app.run()













