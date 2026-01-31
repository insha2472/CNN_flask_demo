import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/abc")
def abc():
    return render_template("abc.html")

@app.route("/<name>")
def name(name):
    return render_template("name.html",name=name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)