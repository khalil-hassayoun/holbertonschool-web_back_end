#!/usr/bin/env python3
"""
a Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    x = len(list(nginx_collection.find()))
    print(x, "logs\nMethods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        print(
            "\tmethod {}: {}".format(
                m, len(list(nginx_collection.find({"method": m})))
                )
            )
    print(
        "{} status check".format(
            len(list(
                nginx_collection.find({"method": "GET", "path": "/status"})
                ))
            )
        )
