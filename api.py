from flask import Flask, jsonify
from storage import episodes, characters, places

app = Flask(__name__)

def character_get(name):
    for n in characters:
        if name == n:
            return characters[name]
        else:
            continue
    return "No Result"

@app.route("/")
def home():
    return "Welcome to the My Little Pony make shift documentation!\n\n"

@app.route("/places/")
def _places():
    q = []
    for n in places:
        q.append(n)
    return jsonify(q)

@app.route("/place/<place>/")
def place(place):
    for n in places:
        if place == n:
            return places[n]
    return "No Result"

@app.route("/episodes/")
def _episodes():
    q = []
    for n in episodes:
        q.append(n)
    return jsonify(q)

@app.route("/episode/<id>/")
def episode(id):
    for n in episodes:
        if id == n:
            return episodes[id]
    return "No Result"

@app.route("/character/<name>/")
def character(name):
    n = character_get(name)
    return n

@app.route("/characters/")
def _characters():
    t = []
    for n in characters:
        t.append(n)
    return jsonify(t)

app.run()
