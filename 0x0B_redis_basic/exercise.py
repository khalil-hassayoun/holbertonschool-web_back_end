#!/usr/bin/env python3
""" Writing strings to Redis  """
from typing import Callable, Optional, Union
import redis
import uuid


class Cache:
    """ Cache class """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random key """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get_str(self, key):
        """  parametrize Cache.get with the correct conversion function """
        return self.get(key, str)

    def get_int(self, key):
        """  parametrize Cache.get with the correct conversion function """
        return self.get(key, int)

    def get(self, key: str, fn: Optional[Callable] = None):
        """ convert the data back to the desired format """
        val = self._redis.get(key)
        return val if not fn else fn(val)
