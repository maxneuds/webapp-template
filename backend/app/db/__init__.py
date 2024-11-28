from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

# Use dynamically generated MongoDB URI
client = AsyncIOMotorClient(settings.mongo_uri)
database = client["webapp-template"]


