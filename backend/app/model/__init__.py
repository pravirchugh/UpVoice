import os

from pymongo.mongo_client import MongoClient

def get_db():
    client = MongoClient(os.getenv('MONGO_DB_DATABASE_URI'))
    database_name = os.getenv('DATABASE_NAME')
    db = client[database_name]
    return db

db = get_db()

# Send a ping to confirm a successful connection
try:
    db.admin.command('ping')
except Exception as e:
    print(e)