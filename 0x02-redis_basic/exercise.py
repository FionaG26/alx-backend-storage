#!/usr/bin/env python3
"""
This module implements a Cache class using Redis for data storage.
"""

import redis
import uuid
import functools


class Cache:
    """
    A cache class that stores data in Redis.
    """

    def __init__(self):
        """
        Initializes the Cache instance and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str) -> str:
        """
        Stores the input data in Redis using a random key and returns the key.

        Args:
            data: The data to be stored. It can be a str, bytes, int, or float.

        Returns:
            The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
        """
        Retrieves the data associated with the given key
        from Redis and optionally converts it to the desired
        format using the provided conversion function.

        Args:
            key: The key associated with the data in Redis.
            fn: Optional conversion function to convert the data to
            the desired format.

        Returns:
            The retrieved data, converted if a conversion function is provided.
            If the key does not exist in Redis, None is returned.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str):
        """
        Retrieves the data associated with the given key
        from Redis as a string.

        Args:
            key: The key associated with the data in Redis.

        Returns:
            The retrieved data as a string.
            If the key does not exist in Redis, None is returned.
        """
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str):
        """
        Retrieves the data associated with the given
        key from Redis as an integer.

        Args:
            key: The key associated with the data in Redis.

        Returns:
            The retrieved data as an integer.
            If the key does not exist in Redis, None is returned.
        """
        return self.get(key, fn=int)


def count_calls(method):
    """
    Decorator that counts the number of times a method is called.

    Args:
        method: The method to be decorated.

    Returns:
        The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the count for
        the method and returns the result.

        Args:
            self: The instance of the class.
            *args: The positional arguments passed to the method.
            **kwargs: The keyword arguments passed to the method.

        Returns:
            The result returned by the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method):
    """
    Decorator that stores the history of inputs and outputs for a method.

    Args:
        method: The method to be decorated.

    Returns:
        The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores the inputs and
        outputs and returns the result.

        Args:
            self: The instance of the class.
            *args: The positional arguments passed to the method.
            **kwargs: The keyword arguments passed to the method.

        Returns:
            The result returned by the original method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper


cache = Cache()


@count_calls
@call_history
def store(self, data: str) -> str:
    """
    Stores the input data in Redis with a random key and returns the key.
    This method is decorated with count_calls and call_history decorators.

    Args:
        data: The data to be stored in Redis.

    Returns:
        The randomly generated key associated with the stored data.
    """
    key = str(uuid.uuid4())
    self._redis.set(key, data)
    return key


def replay(method):
    """
    Displays the history of calls for a particular method.

    Args:
        method: The method to display the history for.
    """
    key = method.__qualname__ + ":inputs"
    inputs = cache._redis.lrange(key, 0, -1)
    key = method.__qualname__ + ":outputs"
    outputs = cache._redis.lrange(key, 0, -1)
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, outp in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode()}) -> {outp.decode()}")


cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
