#!/usr/bin/env python3
"""
a Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    all = list(nginx_collection.find())
    ips = {}
    x = len(all)
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
    for log in all:
        if log.get('ip') and log.get('ip') in ips:
            ips[log.get('ip')] += 1
        elif log.get('ip'):
            ips[log.get('ip')] = 1
    print("IPs:")
    for ip in sorted(ips, key=ips.get, reverse=True)[:10]:
        print("\t{}: {}".format(ip, ips[ip]))
