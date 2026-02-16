from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["academic_advisor"]
students_collection = db["students"]
