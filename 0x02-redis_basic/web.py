#!/usr/bin/env python3

"""
This module provides a function for retrieving the HTML content of a URL
and caching the result.
"""

import requests
import time
from functools import wraps

CACHE_EXPIRATION = 10  # seconds


def cache_expiring(seconds: int):
    """
    Decorator that caches the result of a function with an expiration time.

    Args:
        seconds (int): The expiration time in seconds.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function that caches the result of the decorated function.

            Args:
                *args: Variable length argument list.
                **kwargs: Arbitrary keyword arguments.

            Returns:
                The result of the decorated function.
            """
            key = f"count:{func.__name__}:{args}"
            if key in cache:
                result, timestamp = cache[key]
                if time.time() - timestamp < seconds:
                    return result

            result = func(*args, **kwargs)
            cache[key] = (result, time.time())
            return result

        return wrapper

    return decorator


@cache_expiring(CACHE_EXPIRATION)
def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
