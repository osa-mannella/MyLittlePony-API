from flask import Flask, jsonify
import pprint
from storage import episodes, characters, places

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def _characters():
    t = []
    for n in characters:
        t.append(n)
    return t

def _places():
    q = []
    for n in places:
        q.append(n)
    return q

def _episodes():
    q = []
    for n in episodes:
        q.append(n)
    return q

@app.route("/")
def home():
    characters = _characters()
    places = _places()
    episodes = _episodes()
    info = {
        "/place/<place_name>": places,
        "/episode/<id>": episodes,
        "/character/<name>": characters
    }
    return info

@app.route("/place/<place_name>/")
def place(place_name):
    for n in places:
        if place_name == n:
            return places[n]
    return jsonify(_places())

@app.route("/episode/<episode_name>/")
def episode(episode_name):
    for n in episodes:
        if episode_name == n:
            return episodes[episode_name]
    return jsonify(_episodes())

@app.route("/character/<name>/")
def character(name):
    for n in characters:
        if name == n:
            return characters[name]
        else:
            continue
    return jsonify(_characters())

app.run()
