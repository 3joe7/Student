from flask import Flask, json, jsonify, request
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")

db = cluster["school"]
collection = db["students"]


app = Flask(__name__)


@app.route("/entry", methods=['POST'])
def entry():
    data = request.json
    f_name = data.get('f_name')
    l_name = data.get('l_name')
    gpa = data.get('gpa')

    collection.insert_one({"f_name":f_name, "l_name":l_name, "gpa":gpa})
    return {"message": "Student record added!"}

@app.route("/rank", methods = ['GET'])
def rank():
    #x = collection.find({ 'gpa': { '$gt' : 9 }})
    #a = [{"Name":i["f_name"], "CGPA":i["gpa"] } for i in x]
    try:
        data = request.json
        cgpa = data.get('gpa')
        #cgpa = (request.args.get('gpa'))
        print(cgpa)
        x = collection.find({ 'gpa': { '$gt' : cgpa}})
        a = [{"Name":i["f_name"], "CGPA":i["gpa"] } for i in x]
        return {'The Top Fraggers are: ':a}
    except:
        return {"message":"Not Found!"}

@app.route("/view", methods=["GET"])
def view():
    x = collection.find()
    a = [{"Name":i["l_name"], "CGPA":i["gpa"] } for i in x]
    return a

app.run()