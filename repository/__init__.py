from app import app
from pymongo import MongoClient
client = MongoClient("mongodb+srv://yang_gampang:yang_gampang@cluster.bhvqwrv.mongodb.net/?retryWrites=true&w=majority")
db = client["form_hub"]
collection = db["users_task"]