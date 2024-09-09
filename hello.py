from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hey There '

@app.route("/pal/<name>")
def pal(name):
    return f'Pal {name}!'

app.run()