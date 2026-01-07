from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    client: Optional[AsyncIOMotorClient] = None
    
    @classmethod
    def get_client(cls) -> AsyncIOMotorClient:
        """Get MongoDB client instance"""
        if cls.client is None:
            mongodb_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
            cls.client = AsyncIOMotorClient(mongodb_url)
        return cls.client
    
    @classmethod
    def get_database(cls):
        """Get database instance"""
        client = cls.get_client()
        db_name = os.getenv("DATABASE_NAME", "website_generator")
        return client[db_name]
    
    @classmethod
    async def close_connection(cls):
        """Close MongoDB connection"""
        if cls.client:
            cls.client.close()
            cls.client = None


async def get_database():
    """Dependency for FastAPI routes"""
    return Database.get_database()
