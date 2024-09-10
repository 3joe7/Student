from flask import Flask, request

from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017")
db = cluster["school"]
collection = db["student"]

app = Flask(__name__)

@app.route("/entry", methods = ['POST'])
def entry():
    data = request.json
    f_name = data.get('f_name')
    l_name = data.get('l_name')
    gpa = data.get('gpa')

    collection.insert_one({"f_name":f_name, "l_name":l_name, "gpa":gpa})
    return {"Message" : "Record added succesfully!"}

@app.route("/view", methods = ['GET'])
def view():
    x = collection.find()
    a = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x]
    return a

@app.route("/rank", methods =['GET'])
def rank():
    '''try:
        #data = request.json
        #grade = data.get('grade')
        #grade = request.args.get('grade')'''

    x1 = collection.find({'$and': [{'gpa' :{'$gte':9}}, {'gpa': {'$lte':10}}]})
    a1 = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x1]
    #return {"The A1 holders are: ": a1}

    x2 = collection.find({'$and': [{'gpa' :{'$gte':8}}, {'gpa': {'$lte':9}}]})
    a2 = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x2]
    #return {"The A2 holders are: ": a2}

    x3 = collection.find({'$and': [{'gpa' :{'$gte':7}}, {'gpa': {'$lte':8}}]})
    a3 = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x3]
    #return {"The B1 holders are: ": a3}

    x4 = collection.find({'$and': [{'gpa' :{'$gte':6}}, {'gpa': {'$lte':7}}]})
    a4 = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x4]
    #return {"The B2 holders are: ": a4}

    x5 = collection.find({'gpa': {'$lte':6}})
    a5 = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x5]
    #return {"The  Underperformers are: ": a5} 

    return {"The A1 holders are: ":a1, "The A2 holders are: ": a2, "The B1 holders are: ": a3, "The B2 holders are: ": a4, "The underperformers are: ": a5}

    #return {"Record Not Found!"}

@app.route("/getrank", methods =['GET'])
def get_rank():
    try:
        #data = request.json
        #grade = data.get('grade')
        grade = request.args.get('grade')

        if grade == 'A1':
            x = collection.find({'$and': [{'gpa' :{'$gte':9}}, {'gpa': {'$lte':10}}]})
            a = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x]
            return {"The A1 holders are: ": a}
        elif grade == 'A2':
            x = collection.find({'$and': [{'gpa' :{'$gte':8}}, {'gpa': {'$lte':9}}]})
            a = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x]
            return {"The A2 holders are: ": a}
        elif grade == 'B1':
            x = collection.find({'$and': [{'gpa' :{'$gte':7}}, {'gpa': {'$lte':8}}]})
            a = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x]
            return {"The B1 holders are: ": a}
        elif grade == 'B2':
            x = collection.find({'$and': [{'gpa' :{'$gte':6}}, {'gpa': {'$lte':7}}]})
            a = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x]
            return {"The B2 holders are: ": a}
        else:
            x = collection.find({'gpa': {'$lte':6}})
            a = [{"Name:":i["l_name"], "CGPA:":i["gpa"]} for i in x]
            return {"The  Underperformers are: ": a}
    except:
        return {"Record Not Found!"}
    
@app.route("/cgpa", methods = ['GET'])
def cgpa():
    #x = collection.find({ 'gpa': { '$gt' : 9 }})
    #a = [{"Name":i["f_name"], "CGPA":i["gpa"] } for i in x]
    try:
        #data = request.json
        #cgpa = data.get('gpa')
        cgpa = int(request.args.get('cgpa'))
        x = collection.find({ 'gpa': { '$gt' : cgpa}})
        a = [{"Name":i["f_name"], "CGPA":i["gpa"] } for i in x]
        return {'The students with more than {cgpa} are: ':a}
    except:
        return {"message":"Not Found!"}

app.run()