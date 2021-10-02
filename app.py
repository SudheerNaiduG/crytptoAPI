from flask import Flask
from flask_restful import Api,Resource,reqparse
import pymongo
import json
client=pymongo.MongoClient("ENTER YOUR MONGODB URL HERE TO UPDATE THE DB WITH THE PRICES")
db=client.price.crypto

app=Flask(__name__)
api=Api(app)

class Price(Resource):
	def get(self,coin="None"):
		
		if coin=="None":
			return "No currency parameter found in the GET request",404
		
		ans=db.find_one({"market_name":coin.upper()},{'_id':0})
		
		if ans is not None:
			return json.loads(json.dumps(ans)),200
		
		return "Please Enter a valid currency from wazirx.com",404

api.add_resource(Price,"/wazirx","/wazirx/","/wazirx/<string:coin>")
if __name__=="__main__":
	print("Creating Thread")
	thread=threading.Thread(target=api)
	print("Starting Thread")
	thread.start()
	print("Thread started and scraping wazirx.com")
	print("Starting flask app")
	app.run(debug=True)
