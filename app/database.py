from pymongo import ASCENDING

from motor.motor_asyncio import AsyncIOMotorClient
import aioredis

from config import settings


class Database:
    client: AsyncIOMotorClient | None = None
    db = None
    redis = None


database = Database()


async def connect_db():
    database.client = AsyncIOMotorClient(settings.MONGO_URL)
    database.db = database.client.messages_db
    database.redis = await aioredis.create_redis_pool(settings.REDIS_URL)
    await database.db.messages.create_index([('created_at', ASCENDING)])


async def disconnect_db():
    database.client.close()
    database.redis.close()
    await database.redis.wait_closed()
