from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file
print("MONGO URI:", os.getenv("MONGO_URI"))

client = MongoClient(os.getenv("MONGO_URI"))  # Connect to MongoDB
db = client["ecommerce"]  # Use 'ecommerce' database

products_collection = db["products"]
orders_collection = db["orders"]
