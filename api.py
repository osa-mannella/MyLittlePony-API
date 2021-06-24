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

places = {
    "cystal empire": {
        "description": "The Crystal Empire is a location that first appears in the two-part third season premiere of My Little Pony Friendship is Magic as the home of the Crystal Ponies. It is ruled by Princess Cadance and Prince Shining Armor and formerly Princess Amore and King Sombra.",
        "ruler": "Princess Cadance and Prince Shining Armor"
        "first-appearance": "Season 3 Episode 1"
    },
    "equestria": {
        "description": "Equestria is the main setting of the My Little Pony Friendship is Magic franchise. Equestria is inhabited by magical ponies and other talking creatures, such as griffons and dragons. Other animals and creatures also live in Equestria. Equestria is called a kingdom in the first episode of the show and in other media, though it does contain other \"kingdoms\" within it such as the Crystal Empire; the show and other media take place in many locations and their exact affiliation with Equestria is not explored. Equestria was co-ruled by Princess Celestia and Princess Luna, who resided in a palace in the city of Canterlot until The Last Problem, when they retire with Twilight Sparkle taking their place. The name \"Equestria\" is derived from the word \"equestrian\", which denotes a relation to horseback riding. Consequently, it also has an origin in equus, the Latin word for \"horse.\"",
        "ruler": "Princess Celestia and Princess Luna, after Season 9 Episode 26 Twilight Sparkle",
        "first-appearance": "Season 1 Episode 1"
    },
    "ponyville": {
        "description": "Ponyville is a town in Equestria, the main setting of the series My Little Pony Friendship is Magic, and home to the leading characters. Ponyville is first featured in the first episode and is the setting for most of the episodes.",
        "ruler": "N/A",
        "first-appearance": "Season 1 Episode 1"
    },
    "everfree forest": {
        "description": "The Everfree Forest is a wild wooded area on the outskirts of Ponyville that is introduced in Friendship is Magic, part 2. It is presented as a mysterious place that is home to a variety of creatures and animals, and it possesses a quality that allows plants and animals to thrive without pony intervention, which ponies consider "unnatural". It is also where Zecora makes her residence and contains other locations such as the Castle of the Two Sisters and the Tree of Harmony.",
        "ruler": "N/A",
        "first-appearance": "Season 1 Episode 2"
    },
    "canterlot": {
        "description": "Canterlot is a city first featured in the series' premiere episode as the residence of Twilight Sparkle, where she studies under Princess Celestia. The city holds the royal castle, making it the capital of Equestria. It is also the venue of important cultural events like the Grand Galloping Gala. The name of the city is a portmanteau of "canter," a three-beat horse gait, and Camelot, a British kingdom from Arthurian legends.",
        "ruler": "Princess Celestia, Twilight Sparkle after Season 9 Episode 26",
        "first-appearance": "Season 1 Episode 1"
    }
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
        t.append(n)
    return jsonify(t)

app.run()
