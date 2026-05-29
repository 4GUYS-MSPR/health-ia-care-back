from pymongo import MongoClient

from django.conf import settings

from core.utils.response import JsonResponse
from core.utils.logger import logger

class DB:
    def __init__(
        self,
        uri=f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/?authSource={settings.MONGO_AUTH_SOURCE}&directConnection=true",
        db_name=settings.MONGO_DBNAME
    ):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

        self.users = self.db["users"]
        self.logs = self.db["logs"]

        self.client.admin.command('ping')

    def close(self):
        self.client.close()

def test():
    try:
        logger.log.info("Tentative de connexion...")
        client = MongoClient(
            f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/?authSource={settings.MONGO_AUTH_SOURCE}&directConnection=true",
            serverSelectionTimeoutMS=3000
        )
        client.admin.command('ping')
        return JsonResponse.response("Connexion MongoDB réussie ! 🔥", 200)
    except Exception as e:
        logger.log.error(f"Échec de la connexion : {e}")
        return JsonResponse.response(f"Échec de la connexion : {e}", 500)
