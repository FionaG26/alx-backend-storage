#!/usr/bin/env python3
"""
8-all.py
"""


def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of documents in the collection.
        An empty list if no documents are found.
    """
    documents = list(mongo_collection.find())
    return documents
