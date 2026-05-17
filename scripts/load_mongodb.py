from pymongo import MongoClient
import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.transform import transform_function

# Connection string



try:
    def load_function():
        with MongoClient("mongodb://192.168.64.1/") as client:
            db = client["my-database"]
            collection = db["Restaurants"]
            df = transform_function().to_dict(orient="records")

            collection.delete_many({})
            collection.insert_many(df)


except Exception as e:
    print(f"Connection failed: {e}")