#!/usr/bin/env python3
"""
Inserts a new document into a collection based on keyword arguments.
"""

from pymongo.collection import Collection

def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """
    Inserts a new document into the given MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Keyword arguments representing the fields and values of the document.

    Returns:
        The new _id of the inserted document.
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id


if __name__ == "__main__":
    pass  # Add any necessary code or tests here
