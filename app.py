import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/identity")
def identity():
    return render_template("identity.html")

@app.route("/gossip")
def gossip():
    return render_template("gossip.html")

@app.route("/events")
def events():
    return render_template("events.html")
#
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
#
@app.route("/abc")
def abc():
    return render_template("abc.html")

@app.route("/name/<name>")
def name(name):
    return render_template("name.html", name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)