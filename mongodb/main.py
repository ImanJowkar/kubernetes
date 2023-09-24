import pymongo
from pymongo import MongoClient
from decouple import config


USER=config('USER')
PASSWORD=config('PASSWORD')
MONGO_HOST=config('MONGO_HOST')
MONGO_PORT=config('MONGO_PORT', cast=int)


def get_database():
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = f"mongodb://{USER}:{PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/my-app?authSource=admin&replicaSet=rs0&directConnection=true"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()