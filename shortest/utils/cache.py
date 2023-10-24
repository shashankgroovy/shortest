import redis

from shortest.config import get_settings


class Cache:
    """A wrapper around redis for easy access to cache"""

    config: dict
    client: redis.Redis

    def __init__(self):
        settings = get_settings()
        self.client = redis.Redis(
            host=settings.redis_host,
            port=int(settings.redis_port),
            db=int(settings.redis_db),
        )

    def get(self, key):
        """Syntactic sugar for getting a key's value"""
        return self.client.get(key)

    def set(self, key, value):
        """Syntactic sugar for setting a key-value pair"""
        return self.client.set(key, value)

    def delete(self, key):
        """Syntactic sugar for deleting a key"""
        return self.client.get(key)


# Initalize the default cache
cache = Cache()
