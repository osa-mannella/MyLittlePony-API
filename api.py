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
    return "All information used belongs to the my little pony fandom (https://mlp.fandom.com/wiki/My_Little_Pony_Friendship_is_Magic_Wiki)"

@app.route("/episode/<id>/")
def episode(id):
    for n in episodes:
        if id == n:
            return episodes[id]
        else:
            continue
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
