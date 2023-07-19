#!/usr/bin/env python3

"""
Main file
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache class.

        Creates an instance of the Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a randomly generated key.

        Args:
            data: The data to be stored. Can be a str, bytes, int, or float.

        Returns:
            The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
