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

episodes = {
    "S01E01": {
        "title": "Friendship is Magic, part 1",
        "description": "Under Princess Celestia's instructions, Twilight Sparkle goes to Ponyville to supervise the preparations for the Summer Sun Celebration and make some friends. However, Twilight is preoccupied with the impending return of Nightmare Moon from her thousand-year banishment.",
        "writer": "Lauren Faust",
        "release-date": "2010-10-10",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/9/9f/Twilight_looks_up_at_the_moon_S1E01.png/revision/latest/scale-to-width-down/250?cb=20121209043547"
    },
    "S01E02": {
        "title": "Friendship is Magic, part 2",
        "description": "In this episode, Twilight Sparkle and her new friends travel to the Castle of the Two Sisters to retrieve the Elements of Harmony in the hope of stopping Nightmare Moon from taking over Equestria.",
        "writer": "Lauren Faust",
        "release-date": "2010-10-22",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/2/2c/Main_ponies_activated_the_Elements_of_Harmony_S01E02.png/revision/latest/scale-to-width-down/250?cb=20111205172131"
    },
    "S01E03": {
        "title": "The Ticket Master",
        "description": "The Ticket Master is the third episode of the first season of My Little Pony Friendship is Magic. Princess Celestia gives Twilight Sparkle two tickets to the Grand Galloping Gala. However, all of Twilight’s friends want to attend the gala.",
        "writer": "	Amy Keating Rogers & Lauren Faust",
        "release-date": "2010-10-29",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/3/37/Twilight_Sparkle_overjoyed_about_tickets_S1E03.png/revision/latest/scale-to-width-down/250?cb=20130103015746"
    },
    "S01E04": {
        "title": "Applebuck Season",
        "description": "Applebuck Season is the fourth episode of the first season of My Little Pony Friendship is Magic. In this episode, Applejack attempts to harvest the apple crop in Sweet Apple Acres by herself because her brother, Big McIntosh, is injured. However, her stubbornness and sleep deprivation cause problems all over Ponyville. Hasbro started packaging a DVD of this episode with certain pony toys in January 2012.",
        "writer": "Amy Keating Rogers",
        "release-date": "2010-11-05",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/8/85/Big_McIntosh_and_Applejack_looking_at_Sweet_Apple_Acres_S01E04.png/revision/latest/scale-to-width-down/250?cb=20200311194616"
    },
    "S01E05": {
        "title": "Griffon the Brush Off",
        "description": "Griffon the Brush Off is the fifth episode of the first season of My Little Pony Friendship is Magic. In this episode, Pinkie Pie and Rainbow Dash bond by playing pranks on the other ponies, but when Rainbow Dash's old friend, Gilda the griffon, shows up for a visit, Pinkie gets left out. The title is a play on the phrase \"given the brush-off\", which is an abrupt and rude dismissal.",
        "writer": "Cindy Morrow",
        "release-date": "2010-11-12",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/5/57/Gilda_pointing_at_Pinkie_S1E5.png/revision/latest/scale-to-width-down/250?cb=20130106052926"
    },
    "S01E06": {
        "title": "Boast Busters",
        "description": "Boast Busters is the sixth episode of the first season of My Little Pony Friendship is Magic. In this episode, a new unicorn going by the name of \"The Great and Powerful Trixie\" arrives in Ponyville, claiming to be the greatest pony in all of Equestria. The title of the episode is a play on the title of the Ghostbusters franchise.",
        "writer": "	Chris Savino",
        "release-date": "2010-11-19",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/a/ab/Trixie%27s_flashy_stage_S1E06.png/revision/latest/scale-to-width-down/250?cb=20121009174325"
    },
    "S01E07": {
        "title": "Dragonshy",
        "description": "Dragonshy is the seventh episode of the first season of My Little Pony Friendship is Magic. In this episode, a sleeping dragon's smoke disrupts the skies of Equestria and the Mane Six are tasked by Princess Celestia to convince it to leave, much to Fluttershy's displeasure. The episode's title is a portmanteau of Dragon and Fluttershy.",
        "writer": "	Meghan McCarthy",
        "release-date": "2010-11-26",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/5/51/Fluttershy_notices_the_smoke_S01E07.png/revision/latest/scale-to-width-down/250?cb=20130103050304"
    },
    "S01E08": {
        "title": "Look Before You Sleep",
        "description": "Look Before You Sleep is the eighth episode of the first season of My Little Pony Friendship is Magic. In this episode, Applejack and Rarity are forced to stay at the library where Twilight resides for the night due to a thunderstorm. Twilight takes this opportunity to drag them into having a slumber party. The title of the episode is a play on the saying look before you leap, meaning acting only after careful planning.",
        "writer": "Charlotte Fullerton",
        "release-date": "2010-12-03",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/c/ce/Rarity%2C_Applejack_and_Twilight_makeovers_S01E08.png/revision/latest/scale-to-width-down/250?cb=20200313112345"
    },
    "S01E09": {
        "title": "Bridle Gossip",
        "description": "Bridle Gossip is the ninth episode of the first season of My Little Pony Friendship is Magic. In this episode, Twilight Sparkle and her friends encounter Zecora, a mysterious zebra who lives in the Everfree Forest. The title of the episode is a play on the phrase \"idle gossip\".",
        "writer": "Amy Keating Rogers",
        "release-date": "2010-12-10",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/f/ff/Zecora_S01E09.png/revision/latest/scale-to-width-down/250?cb=20130103054500"
    },
    "S01E10": {
        "title": "Swarm of the Century"
        "description": "Swarm of the Century is the tenth episode of the first season of My Little Pony Friendship is Magic. In this episode, a swarm of pests called parasprites find their way into Ponyville, causing chaos and threatening to ruin Princess Celestia's visit to the town.",
        "writer": "M. A. Larson",
        "release-date": "2010-12-17",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/e/ef/Main_ponies_at_Fluttershy%27s_cottage_looking_nervous_S1E10.png/revision/latest/scale-to-width-down/250?cb=20200313032202"
    },
    "S01E11": {
        "title": "Winter Wrap Up",
        "description": "Winter Wrap Up is the eleventh episode of the first season of My Little Pony Friendship is Magic. In this episode, winter comes to an end, and Ponyville prepares for an annual clean-up to make way for spring.",
        "writer": "Cindy Morrow",
        "release-date": "2010-12-24",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/3/3b/Spotlight_on_Twilight_Sparkle_S1E11.png/revision/latest/scale-to-width-down/250?cb=20200313205106"
    },
    "S01E12": {
        "title": "Call of the Cutie",
        "description": "Call of the Cutie is the twelfth episode of the first season of My Little Pony Friendship is Magic. In this episode, Apple Bloom becomes concerned about her lack of a cutie mark and tries to earn it before an upcoming party. At the party, she ends up befriending Scootaloo and Sweetie Belle, and they form the Cutie Mark Crusaders.",
        "writer": "Meghan McCarthy",
        "release-date": "2011-01-07",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/b/b3/Apple_Bloom%27s_blank_flank_is_revealed_S1E12.png/revision/latest/scale-to-width-down/250?cb=20130106090036"
    },
    "S01E13": {
        "title": "Fall Weather Friends",
        "description": "Fall Weather Friends is the thirteenth episode of the first season of My Little Pony Friendship is Magic. In this episode, Applejack and Rainbow Dash's sportsmanship is put to the test as they face off in an Iron Pony competition to see who the better athlete is. The title is a play on fair weather friends, which refers to people who are only friends when it is convenient (when weather is fair) and will abandon their friends during bad times.",
        "writer": "Amy Keating Rogers",
        "release-date": "2011-01-28",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/3/3a/Applejack_%26_Rainbow_brohoof_S1E13.png/revision/latest/scale-to-width-down/250?cb=20120310072234"
    },
    "S01E14": {
        "title": "Suited For Success",
        "description": "Suited For Success is the fourteenth episode of the first season of My Little Pony Friendship is Magic. In this episode, Rarity wants to make dresses for her friends for the upcoming Grand Galloping Gala, but has trouble satisfying all their requests. The title of the episode is a play on \"dressed for success\"; the word 'suited' here both refers to the original phrase, as well as the meaning of 'being appropriate'.",
        "writer": "Charlotte Fullerton"
        "release-date": "2011-02-04",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/1/12/Rarity_being_overwhelmed_with_pressure_S1E14.png/revision/latest/scale-to-width-down/250?cb=20200313112450"
    },
    "S01E15": {
        "title": "Feeling Pinkie Keen",
        "description": "Feeling Pinkie Keen is the fifteenth episode of the first season of My Little Pony Friendship is Magic. In this episode, Twilight Sparkle learns that Pinkie Pie has an unusual ability to sense happenings in the immediate future, known as \"Pinkie Sense.\" The title of the episode is a play on the phrase \"feeling peachy keen,\" which refers to one feeling upbeat and generally happy.",
        "writer": "Dave Polsky",
        "release-date": "2011-02-11",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/f/f7/Pinkie_vibrating_S01E15.png/revision/latest/scale-to-width-down/250?cb=20200313050645"
    },
    "S01E16": {
        "title": "Sonic Rainboom",
        "description": "Sonic Rainboom is the sixteenth episode of the first season of My Little Pony Friendship is Magic. Rainbow Dash is worried about her performance in the Best Young Flyer competition, but she pulls off a sonic rainboom, impressing the crowd.",
        "writer": "	M. A. Larson",
        "release-date": "2011-02-18",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/b/be/Rainbow_Dash_performing_Sonic_Rainboom_S01E16.png/revision/latest/scale-to-width-down/250?cb=20130103074703"
    },
    "S01E17": {
        "title": "Stare Master",
        "description": "Stare Master is the seventeenth episode of the first season of My Little Pony Friendship is Magic. In this episode, Fluttershy offers to take care of the Cutie Mark Crusaders, but things take a frightening turn when the Crusaders venture into the Everfree Forest. This is the first and only episode in season one where Applejack does not appear, as well as not being with Apple Bloom. The episode's title is a play on the American exercise machine company StairMaster.",
        "writer": "Chris Savino",
        "release-date": "2011-02-25	",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/6/64/Fluttershy_staring_at_chickens_S01E17.png/revision/latest/scale-to-width-down/250?cb=20200312150751"
    },
    "S01E18": {
        "title": "The Show Stoppers",
        "description": "The Show Stoppers is the eighteenth episode of the first season of My Little Pony Friendship is Magic. In this episode, the Cutie Mark Crusaders believe that winning a talent show will help them earn their cutie marks. The title of this episode may be literally referencing the Cutie Mark Crusaders' antics, in which they perform a theatrical showstopper - a performance that garners enthusiastic or prolonged applause, which usually forces the performers to stop the performance until it has died down. An alternate meaning in business terms, however, is an action or event that puts a halt to all other activities until it can be resolved.",
        "writer": "Cindy Morrow",
        "release-date": "2011-03-04",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/b/b3/Cutie_Mark_Crusaders_song_S1E18.png/revision/latest/scale-to-width-down/250?cb=20200310155020"
    },
    "S01E19": {
        "title": "A Dog and Pony Show",
        "description": "A Dog and Pony Show is the nineteenth episode of the first season of My Little Pony Friendship is Magic. In this episode, Rarity is searching for a new load of gems with Spike's assistance. However, when a group of creatures called the Diamond Dogs abduct Rarity, Spike and the other ponies head into the Dogs' underground burrows to rescue her.",
        "writer": "Amy Keating Rogers",
        "release-date": "2011-03-11",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/f/f6/Rarity_in_front_of_the_Diamond_Dogs_S1E19.png/revision/latest/scale-to-width-down/250?cb=20130104080716"
    },
    "S01E20": {
        "title": "Green Isn't Your Color",
        "description": "Green Isn't Your Color is the twentieth episode of the first season of My Little Pony Friendship is Magic. Photo Finish, a fashion photographer, hires Fluttershy to be her model. However, Photo Finish ignores Rarity's dress work. Despite her jealousy, Rarity urges Fluttershy to seize the opportunity. Fluttershy dislikes modeling due to her having no confidence in herself but doesn't want to disappoint Rarity after she has encouraged Fluttershy so heavily.",
        "writer": "Meghan McCarthy",
        "release-date": "2011-03-18",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/f/f8/Fluttershy_photoshoot_2_S1E20.png/revision/latest/scale-to-width-down/250?cb=20130711192135"
    },
    "S01E21": {
        "title": "Over a Barrel",
        "description": "Over a Barrel is the twenty-first episode of the first season of My Little Pony Friendship is Magic. The idiom \"over a barrel\" means being in a helpless position where others are in control. In this episode, the Mane Six and Spike separate and are caught in a dispute between a western town's settler-ponies and the native buffalo herd.",
        "writer": "Dave Polsky",
        "release-date": "2011-03-25",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/6/67/Appleloosa_Preparing_For_Battle_S1E21.png/revision/latest/scale-to-width-down/250?cb=20200311194311"
    },
    "S01E22": {
        "title": "A Bird in the Hoof",
        "description": "A Bird in the Hoof is the twenty-second episode of the first season of My Little Pony Friendship is Magic. In this episode, during a visit from Princess Celestia, Fluttershy sees the Equestrian royal's sick bird and decides to take her home to look after. The episode title is a play on the proverb \"a bird in the hand is worth two in the bush,\" meaning it is better to stick with something one already has, rather than pursuing something one may never get.",
        "writer": "Charlotte Fullerton",
        "release-date": "2011-04-08",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/f/ff/Fluttershy_holding_Philomena_S01E22.png/revision/latest/scale-to-width-down/250?cb=20200312150711"
    },
    "S01E23": {
        "title": "The Cutie Mark Chronicles",
        "description": "The Cutie Mark Chronicles is the twenty-third episode of the first season of My Little Pony Friendship is Magic. In this episode, the Cutie Mark Crusaders learn how each of the Mane Six acquired their cutie marks. This is the first episode in which all of the members of the CMC and all of the leading characters have a speaking role.",
        "writer": "M. A. Larson",
        "release-date": "2011-04-15",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/c/c0/Rainbow_Dash_shows_her_cutie_mark_S01E23.png/revision/latest/scale-to-width-down/250?cb=20130103072422"
    },
    "S01E24": {
        "title": "Owl's Well That Ends Well",
        "description": "Owl's Well That Ends Well is the twenty-fourth episode of the first season of My Little Pony Friendship is Magic. The title of the episode is a play on the phrase, \"All's Well That Ends Well.\" In this episode, Twilight Sparkle befriends an owl who becomes her second personal assistant, to the displeasure of Spike.",
        "writer": "Cindy Morrow",
        "release-date": "2011-04-22",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/6/6a/Spike_%27Got_it%21%27_S1E24.png/revision/latest/scale-to-width-down/250?cb=20130104084345"
    },
    "S01E25": {
        "title": "Party of One",
        "description": "Party of One is the twenty-fifth episode of the first season of My Little Pony Friendship is Magic. In this episode, Pinkie Pie investigates her friends’ excuses for not attending one of her parties.",
        "writer": "Meghan McCarthy",
        "release-date": "2011-04-29",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/f/f8/Pinkie_Pie_surrounded_by_darkness_under_a_cone_of_light_S01E25.png/revision/latest/scale-to-width-down/250?cb=20130102101302"
    },
    "S01E26": {
        "title": "The Best Night Ever",
        "description": "The Best Night Ever is the twenty-sixth and final episode of season one of My Little Pony Friendship is Magic. In this episode, Twilight Sparkle and her friends attend the Grand Galloping Gala, but none of their experiences meet their expectations, much to their disappointment.",
        "writer": "Amy Keating Rogers",
        "release-date": "2011-05-06",
        "thumbnail": "https://static.wikia.nocookie.net/mlp/images/2/20/Main_Six_determined_to_have_the_Best_Night_Ever_S1E26.png/revision/latest/scale-to-width-down/250?cb=20200313041316"
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
