#!/usr/bin/env python3
"""
Returns all students sorted by average score.
"""

from pymongo.collection import Collection

def top_students(mongo_collection: Collection):
    """
    Retrieves all students from the given MongoDB collection
    and returns them sorted by average score.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of student documents sorted by average score.
        Each document will have an additional key 'averageScore'
        representing the average score.
    """
    students = list(mongo_collection.find())

    for student in students:
        topics = student.get('topics', [])
        total_score = sum(topic['score'] for topic in topics)
        average_score = total_score / len(topics) if len(topics) > 0 else 0
        student['averageScore'] = average_score

    return sorted(students, key=lambda s: s['averageScore'], reverse=True)
