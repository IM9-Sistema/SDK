from json import loads

import redis
from pydantic import BaseModel

from ..structures import RedisConfig

class Redis:
    def __init__(self, host='localhost', port=6379, db=0, pooled: bool = None, min_size: int = None, max_size: int = None):
        self._pool = None
        self._connection = None
        self.host = host
        self.port = port
        self.pooled = pooled
        self.db = db
        self.min_size = min_size
        self.max_size = max_size

    @property
    def connection(self):
        if not self._connection:
            if not self.pooled:
                self._connection = redis.Redis(host=self.host, port=self.port, db=self.db)
            else:
                self._pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, max_connections=self.max_size)
        return self._connection if not self.pooled else redis.Redis.from_pool(self._connection)

    @classmethod
    def from_config(cls, config: RedisConfig):
        return cls(host=config.host, port=config.port, db=config.database, pooled=True if config.pool else False, min_size=config.pool.min_size if config.pool else None, max_size=config.pool.max_size if config.pool else None)

    def get(self, key):
        return self.connection.get(key)

    def set(self, key, value, ttl: int = None):
        if isinstance(value, BaseModel):
            value = value.model_dump_json().encode('utf-8')
        self.connection.set(key, value, ex=ttl)

    def memo(self, identifier: str, ttl: int, casting):
        def wrapper(func):
            def inner_wrapper(*args, **kwargs):
                if data := self.get(f'{identifier}::{args}::{kwargs}'):
                    return casting(data)
                data = func(*args, **kwargs)
                self.set(f'{identifier}::{args}::{kwargs}', data, ttl)
                return data
            return inner_wrapper
        return wrapper

