#!/usr/bin/env python3
""" a Python function that inserts a new document in a collection
based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ a Python function that inserts a new document in a collection
    based on kwargs """
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
