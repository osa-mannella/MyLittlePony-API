from flask import Flask

app = Flask(__name__)

def characters(name):
    characters = {
        "jack": {
            "age": 15,
            "name": "Jack",
            "height": "5' 11",
            "eye_color": "Blue",
        },
        "jill": {
            "age": 14,
            "name": "Jill",
            "height": "5' 5",
            "eye_color": "Blue",
        },
    }
    for n in characters:
        if name == n:
            return characters[name]
        else:
            continue
    return "No Result"

@app.route("/character/<name>/")
def character(name):
    n = characters(name)
    return n

app.run()
