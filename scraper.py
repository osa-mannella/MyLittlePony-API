from bs4 import BeautifulSoup
import requests
from pprint import pprint

mlp = {}

r = requests.get("https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media")

soup = BeautifulSoup(r.text, "html.parser")
n = soup.find_all("table")
for q in n:
    k = q.find_all("td")
    num = -5
    while True:
        try:
            if len(mlp) == 221:
                break
            num = num + 6
            zr = k[num]
            episode_name = zr.a['title']
            url = "https://mlp.fandom.com"
            mlp_url = url + zr.a['href']
            mlp[episode_name] = mlp_url
        except IndexError:
            break

def date(episode: int):
    r = requests.get('https://mlp.fandom.com/wiki/Friendship_is_Magic_animated_media#Season_seven')

    soup = BeautifulSoup(r.text, "html.parser")

    tables = soup.find_all("table", class_='table-dotted-rows sortable')

    dates = []
    for table in tables[:9]:
        td = table.find_all('td')
        dates.extend([t.text for t in td[3::6]])
    episode = episode - 1
    r = dates[episode]
    return r[:-1]

episodes = {}

for name in mlp:
    url = mlp[name]
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    paragraph = soup.find_all('p')
    r = paragraph[1].find_next('h2')
    if r.text == "Contents":
        description = paragraph[0].text + paragraph[1].text
    if r.text == "Summary":
        description = paragraph[0].text
    title = soup.find('h1').text
    description = " ".join(description.split())
    table = soup.find('table', class_="infobox")
    td = table.find_all('td')
    episode = td[2].text
    writer = td[5].text[:-1]
    if "20" in writer:
        writer = td[6].text[:-1]
    if int(episode) <= 9:
        episode = "0" + str(episode)
    season = td[1].text
    ident = f"S0{season[:-1]}E{episode[:-1]}"
    identifier = " ".join(ident.split())
    url = td[0].a['href']
    airdate = date(int(td[2].text))
    episodes[identifier] = {
        "title": title,
        "description": description,
        "writer": writer,
        "release-date": airdate,
        "thumbnail": url
    }

pprint(episodes)