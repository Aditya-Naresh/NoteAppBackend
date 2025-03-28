from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from noteapp_server.models import User, Note

MONGO_URI ='mongodb://localhost:27017'

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client.blog, document_models=[User, Note])


