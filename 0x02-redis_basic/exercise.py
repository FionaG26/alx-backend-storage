#!/usr/bin/env python3

"""
This module provides a Cache class that interacts with Redis
to store and retrieve data.
"""

import redis
from typing import Callable, Union


class Cache:
    """
    Cache class for interacting with Redis.
    """

    def __init__(self):
        self.redis_client = redis.Redis()

    def store(self, value: Union[str, bytes, int]) -> str:
        """
        Store the value in Redis and return the generated key.
        """
        key = str(hash(value))
        self.redis_client.set(key, value)
        return key

    def get(
        self, key: str, fn: Callable = None
    ) -> Union[str, bytes, int, None]:
        """
        Retrieve the value from Redis using the given key.
        If the key does not exist, return None.
        If a conversion function (fn) is provided, apply
        it to the retrieved value.
        """
        value = self.redis_client.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve the value from Redis using the given key and
        convert it to a string.
        If the key does not exist, return None.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve the value from Redis using the given key and convert
        it to an integer.
        If the key does not exist, return None.
        """
        return self.get(key, fn=int)


if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
