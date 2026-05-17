from pymongo import MongoClient

def high_density_cities():
    with MongoClient("mongodb://192.168.64.1/") as client:
        db = client["my-database"]
        collection = db["Restaurants"]
        results = list(collection.aggregate([{ "$group": { "_id": "$CITY", "count": { "$sum": 1 } } }]))
        print([result for result in results if result["count"] > 500])