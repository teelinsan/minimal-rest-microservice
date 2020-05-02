import json
import os
import pymongo
from bson import ObjectId
from bson.json_util import dumps


class JSONEncoder(json.JSONEncoder):
	"""
	Extend JSON Encoder to support mongoDB id encoding
	"""
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)


class MongoProvider(object):

	def __init__(self):
		"""
		Create the connection with mongoDB
		"""
		self.myclient = pymongo.MongoClient(f"mongodb://{os.environ.get('MONGO_URL', 'localhost')}:{os.environ.get('MONGO_PORT', 27017)}/")
		self.mydb = self.myclient["MyProject"]
		self.mycol = self.mydb["users"]

	def create_user(self, payload):
		"""
		Create a user with the information provided in the payload
		:param payload: dict
			Dictionary passed as input
		:return: (dict, int)
			Response JSON, Error code
		"""
		if self.mycol.count_documents({'id': payload['id']}, limit=1) != 0:
			return {"error": "Found user with existing ID"}, 409
		else:
			self.mycol.insert_one(payload)
			return json.loads(JSONEncoder().encode(payload)), 201

	def read_user(self, user_id):
		"""
		Read a user from the database given its id
		:param user_id: int
			Id of the user
		:return: (dict, int)
			Response JSON, Error code
		"""
		if self.mycol.count_documents({'id': user_id}, limit=1) != 0:
			user_query = {"id": user_id}

			user = self.mycol.find_one(user_query)
			user = JSONEncoder().encode(user)
			return json.loads(user), 200
		else:
			return {"error": "user not found"}, 400

	def update_user(self, payload):
		"""
		Update a user with the information provided in the payload
		:param payload: dict
			Dictionary passed as input
		:return: (dict, int)
			Response JSON, Error code
		"""
		if self.mycol.count_documents({'id': payload['id']}, limit=1) != 0: # Check if user exists in DB
			print("Found a user in DB with this id")
			user_query = {"id": payload['id']}
			new_values = {"$set": payload}

			x = self.mycol.update_one(user_query, new_values)
			if x.modified_count != 0:
				return {"message": "Success"}, 201
			else:
				return {"error": "user not modified"}, 403
		else:
			# user not found
			return {"error": "user not found"}, 409

	def delete_user(self, user_id):
		"""
		Delete a user from the database given its id
		:param user_id: int
			Id of the user
		:return: (dict, int)
			Response JSON, Error code
		"""
		user_query = {"id": user_id}
		x = self.mycol.delete_one(user_query)
		if x.deleted_count != 0:
			return {"message": "Success"}, 200

		else:
			return {"error": "user not found"}, 400
