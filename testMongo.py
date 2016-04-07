# -*- coding:utf-8 -*-

import pymongo

if __name__ == "__main__":
    address = 'xx.xx.xx.xx'
    port = 27017
    client = pymongo.MongoClient(address)
    db = client['test']
    collection = db['test']
    for doc in collection.find():
        print doc