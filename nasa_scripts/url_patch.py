import json

planets = json.load(open("data/planets.json"))
galaxies = json.load(open("data/galaxies.json"))
stars = json.load(open("data/stars.json"))

#planet urls
planet_urls_file = open("data/planet_imgs/compiled_planet_imgs.json", "r")
planet_urls = json.load(planet_urls_file)
planet_urls_file.close()
for item in planet_urls:
    pid = item["pid"];
    url = item["url"];

    for planet in planets:
        if planet["pid"] == pid:
            planet["img_url"] = url
            break

# galaxy urls
galaxies_urls_file = open("data/galaxies/compiled_galaxies_imgs.json", "r")
galaxies_urls = json.load(galaxies_urls_file)
galaxies_urls_file.close()
for item in galaxies_urls:
    pid = item["pid"];
    url = item["url"];

    for galaxy in galaxies:
        if galaxy["pid"] == pid:
            galaxy["img_url"] = url
            break

# star urls
stars_urls_file = open("data/star_imgs/compiled_stars_imgs.json", "r")
stars_urls = json.load(stars_urls_file)
stars_urls_file.close()
for item in stars_urls:
    pid = item["pid"];
    url = item["url"];

    for star in stars:
        if star["pid"] == pid:
            star["img_url"] = url
            break

json.dump(planets, open("data/planets.json", "w"))
json.dump(stars, open("data/stars.json", "w"))
json.dump(galaxies, open("data/galaxies.json", "w"))