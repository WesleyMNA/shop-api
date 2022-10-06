from pymongo import MongoClient

cluster = MongoClient('mongodb://localhost/shop')
db = cluster['shop']
user_collection = db['user']
