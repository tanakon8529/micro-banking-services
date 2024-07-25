import redis
from django.conf import settings

class RedisController:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            password=settings.REDIS_PASSWORD,
            decode_responses=True
        )

    def set_token(self, key, value, expiration):
        self.client.setex(key, expiration, value)

    def get_token(self, key):
        return self.client.get(key)

    def delete_token(self, key):
        self.client.delete(key)
