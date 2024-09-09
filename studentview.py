from flask import Flask, json
from student import entry

app =Flask(__name__)

@app.route("/view", methods=["GET"])
class view():
    def view():
        v = list(collection.find())
        return json.dumps(v)
    
app.run()