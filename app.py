from flask import Flask
import json

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
	return "PennApps bitch"

@app.route("/search/<item>")
def search(item):
	result = {
		'item' : item,
		'store' : 'Walmart',
		'price' : 35.62
	}
	return json.dumps(result)

if __name__ == "__main__":
    app.run()













