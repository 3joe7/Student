
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/")
db = cluster["school"]
collection = db["students"]

def to_find_names(cgpa):
    x = collection.find({'gpa': {'$gt': cgpa}})
    print(x)
    results = list(x)
    a = [{"Name": i["f_name"], "CGPA": i["gpa"]} for i in results]
    return a

print(to_find_names(int(9)))