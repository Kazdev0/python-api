import requests as rq
from flask import Flask, jsonify

app = Flask(__name__)

d = rq.get("https://api.kazdev.ml/dog")
c = rq.get("https://api.kazdev.ml/cat")
f = rq.get("https://api.kazdev.ml/fox?")
p = rq.get("https://api.kazdev.ml/panda")
b = rq.get("https://api.kazdev.ml/bird")


@app.route("/dog")
def dog():
    return jsonify(link=d.json()["link"])

@app.route("/cat")
def cat():
    return jsonify(link=c.json()["link"])

@app.route("/fox")
def fox():
    return jsonify(link=f.json()["link"])


@app.route("/panda")
def panda():
    return jsonify(link=p.json()["link"])


@app.route("/bird")
def bird():
    return jsonify(link=b.json()["link"])

app.run(host='localhost', port=5000, debug=False) 
