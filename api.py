from flask import Flask, jsonify

app = Flask(__name__)

characters = {
    "twilight sparkle": {
        "appearence": "https://imgur.com/a/vgMPz2i",
        "type": "Unicorn (S01-S03), Alicorn S3+",
        "name": "Princess Twilight Sparkle",
        "gender": "Female",
        "age": 27,
        "description": "Twilight Sparkle is the central main character of My Little Pony Friendship is Magic. She is a female unicorn pony who transforms into an Alicorn and becomes a princess in Magical Mystery Cure. She is also the daughter of Twilight Velvet and Night Light, the younger sister of Shining Armor, sister-in-law to Princess Cadance, and paternal aunt to Flurry Heart.",
        "coat-color": "Pale, light grayish mulberry"
    },
    "applejack": {
        "appearence": "https://imgur.com/a/etZvxwl",
        "type": "Earth",
        "name": "Applejack",
        "gender": "Female",
        "age": 28,
        "description": "Applejack is a female Earth pony and one of the main characters of My Little Pony Friendship is Magic. She lives and works at Sweet Apple Acres with her grandmother Granny Smith, her older brother Big McIntosh, her younger sister Apple Bloom, and her dog Winona. She represents the element of honesty.",
        "coat-color": "Brilliant Gamboge"
    },
    "fluttershy": {
        "appearence": "https://imgur.com/a/zHOZDj3",
        "type": "Pegasus",
        "name": "Fluttershy",
        "gender": "Female",
        "age": 20,
        "description": "Fluttershy is a female Pegasus pony and one of the main characters of My Little Pony Friendship is Magic. She lives in a small cottage near the Everfree Forest and takes care of animals, the most prominent of her charges being Angel the bunny. She represents the element of kindness.",
        "coat-color": "Pale, light grayish gold"
    },
    "rarity": {
        "appearence": "https://imgur.com/a/gIIOjH9",
        "type": "Unicorn",
        "name": "Rarity",
        "gender": "Female",
        "age": 22,
        "description": "Rarity is a female unicorn pony and one of the main characters of My Little Pony Friendship is Magic. She is Sweetie Belle's older sister and the subject of Spike's long-term crush. Rarity works as both a fashion designer and a seamstress at her own shop in Ponyville, the Carousel Boutique. She has a white Persian cat named Opalescence. She represents the element of generosity.",
        "coat-color": "Light gray"
    },
    "pinkie pie": {
        "appearence": "https://imgur.com/a/0lWO39U",
        "type": "Earth",
        "name": "Pinkie Pie",
        "gender": "Female",
        "age": 27,
        "description": "Pinkie Pie, full name Pinkamena Diane Pie,[note 2] is a female Earth pony and one of the main characters of My Little Pony Friendship is Magic. She is an energetic and sociable baker at Sugarcube Corner, where she lives on the second floor with her toothless pet alligator Gummy, and she represents the element of laughter",
        "coat-color": "Pale, light grayish raspberry"
    },
    "rainbow dash": {
        "appearence": "https://imgur.com/a/dqMQwrz",
        "type": "Pegasus",
        "name": "Rainbow Dash",
        "gender": "Female",
        "age": 27,
        "description": "Rainbow Dash is a female Pegasus pony and one of the main characters in My Little Pony Friendship is Magic. She maintains the weather and clears the skies in Ponyville. As a huge fan of the Wonderbolts, she becomes a reservist member of the elite flying group in Testing Testing 1, 2, 3 and a full member in Newbie Dash.",
        "coat-color": "Pale, light grayish cerulean"
    },
    "spike": {
        "appearence": "https://imgur.com/a/tnk4b1m",
        "type": "Dragon",
        "name": "Spike",
        "gender": "Male",
        "age": 13,
        "description": "Spike, also known as Spike the Dragon, is a male \"pre-teen\" dragon and one of the seven main characters of My Little Pony Friendship is Magic. He is Twilight Sparkle's best friend and number one assistant.",
        "coat-color": "Light mulberry with light spring budish gray underbelly and light lime green ear fronds"
    },
    "princess celestia": {
        "appearence": "https://imgur.com/a/Er25yqs",
        "type": "Alicorn",
        "name": "Princess Celestia",
        "gender": "Female",
        "age": 10000,
        "description": "Princess Celestia, called Queen Celestia in one comic and early development, is an Alicorn pony, the former co-ruler of Equestria alongside her younger sister Princess Luna, and the adoptive aunt of Princess Cadance.",
        "coat-color": "Light fuchsiaish gray"
    },
    "princess luna": {
        "appearence": "https://imgur.com/a/sh96maO",
        "type": "Alicorn",
        "name": "Princess Luna",
        "gender": "Female",
        "age": "N/A",
        "description": "Princess Luna, known as Nightmare Moon or Night Mare Moon when transformed or under certain other circumstances, is an Alicorn pony, the younger sister of Princess Celestia, and the main antagonist of the season one premiere of My Little Pony Friendship is Magic as Nightmare Moon.",
        "coat-color": "Dark Blue and Grayish phthalo blue"
    },
}

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

@app.route("/character/<name>/")
def character(name):
    n = character_get(name)
    return n

@app.route("/characters/")
def _characters():
    t = []
    for n in characters:
        t.append(n.title())
    return jsonify(t)

app.run()
