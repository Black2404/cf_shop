import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.shop_cf
order_collection = database.get_collection("orders")
user_collection = database.get_collection("users")
product_collection = database.get_collection("products")
table_collection = database.get_collection("tables")