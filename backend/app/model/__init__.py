import os

from pymongo.mongo_client import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://pravirc:pravirc1@clustermain.jwpbamn.mongodb.net/?retryWrites=true&w=majority")
    database_name = 'upvoice'
    db = client[database_name]
    return db

db = get_db()

# Send a ping to confirm a successful connection
try:
    print("Pinged DB!")
    db.admin.command('ping')
except Exception as e:
    print(e)