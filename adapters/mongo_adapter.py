from pymongo import MongoClient

class MongoAdapter:
    def __init__(self, db_uri):
        self.client = MongoClient(db_uri)
        self.db = self.client.get_default_database()

    def add(self, collection_name, data):
        return self.db[collection_name].insert_one(data).inserted_id

    def get(self, collection_name, query):
        return list(self.db[collection_name].find(query))

    def update(self, collection_name, query, update_data):
        return self.db[collection_name].update_many(query, {'$set': update_data})

    def delete(self, collection_name, query):
        return self.db[collection_name].delete_many(query)