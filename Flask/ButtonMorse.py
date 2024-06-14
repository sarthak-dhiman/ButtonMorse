from flask import Flask

app = Flask(BM)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"