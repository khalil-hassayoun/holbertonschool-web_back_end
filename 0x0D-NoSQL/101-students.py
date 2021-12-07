#!/usr/bin/env python3
""" a Python function that returns all students sorted by average score """


def top_students(mongo_collection):
    """ a Python function that returns all students sorted by average score """
    db_students = list(mongo_collection.find())
    students = []
    for st in db_students:
        scores = [t.get('score') for t in st.get('topics')]
        students.append({
            'name': st.get('name'),
            '_id': st.get('_id'),
            'averageScore': sum(scores) / len(scores)
        })
    return sorted(students, key=lambda k: k['averageScore'], reverse=True)
