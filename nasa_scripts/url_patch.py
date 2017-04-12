import json

planets = json.load(open("scraped_data/scraped_planets.json"))
galaxies = json.load(open("scraped_data/scraped_galaxies.json"))
stars = json.load(open("scraped_data/scraped_stars.json"))
satellites = json.load(open("scraped_data/scraped_satellites.json"))						

print("Adding hardcoded elements.")

# hardcode elements

earth = {"pid":planets[len(planets)-1]["pid"] + 1,
         "name":"Earth",
         "diameter":float(12742),
         "ra":0.0,
         "dec":0.0,
         "gravity":9.81,
         "orbital_period":float(365),
         "mass":float(5.972 * (10 ** 24)),
         "temperature":287,
         "img_url":"https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",
         "star_pid":stars[len(stars)-1]["pid"] + 1,
         "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1}

sun = {"pid":stars[len(stars)-1]["pid"] + 1,
       "name":"Sun",
       "diameter":1.3914 * (10 **6),
       "ra":0.49288194,
       "dec":3.1928926,
       "temperature":5778,
       "mass":1.0,
       "img_url": "http://nineplanets.org/images/thesun.jpg",
       "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1}

milky_way = {"pid":galaxies[len(galaxies)-1]["pid"] + 1,
             "name": "Milky Way",
             "ra":17.7533,
             "dec":-47.2833,
             "morph_type":"Spiral",
             "redshift":0.0,
             "size":360.0,
             "img_url": "https://apod.nasa.gov/apod/image/0801/16500feetmilkywaykc2_brunier.jpg"}

planets.append(earth)
stars.append(sun)
galaxies.append(milky_way)

print("Patching data together with pids.")

for p in planets :
    p["galaxy_pid"] = milky_way["pid"]
    if "hostname" in p :
        hostname = p.pop("hostname")

        star_pid = -1;

        for s in stars :
            if s["name"] == hostname :
                star_pid = s["pid"]
                break

    p["star_pid"] = star_pid;

for s in stars :
    s["galaxy_pid"] = milky_way["pid"]

for s in satellites :
    s["planet_pid"] = earth["pid"]
    s["star_pid"] = sun["pid"]
    s["galaxy_pid"] = milky_way["pid"]
		
print("Adding img urls for planets, stars, and galaxies")

#planet urls
planet_urls_file = open("imgs/compiled_planet_imgs.json", "r")
planet_urls = json.load(planet_urls_file)
planet_urls_file.close()
for item in planet_urls:
    pid = item["pid"] + 1;
    url = item["url"];

    for planet in planets:
        if planet["pid"] == pid:
            planet["img_url"] = url
            break

# galaxy urls
galaxies_urls_file = open("imgs/compiled_galaxies_imgs.json", "r")
galaxies_urls = json.load(galaxies_urls_file)
galaxies_urls_file.close()
for item in galaxies_urls:
    pid = item["pid"] + 1;
    url = item["url"];

    for galaxy in galaxies:
        if galaxy["pid"] == pid:
            galaxy["img_url"] = url
            break

# star urls
stars_urls_file = open("imgs/compiled_stars_imgs.json", "r")
stars_urls = json.load(stars_urls_file)
stars_urls_file.close()
for item in stars_urls:
    pid = item["pid"] + 1;
    url = item["url"];

    for star in stars:
        if star["pid"] == pid:
            star["img_url"] = url
            break

planet_file = open("data/planets.json", "w")
star_file = open("data/stars.json", "w")
galaxy_file = open("data/galaxies.json", "w")
satellite_file = open("data/satellites.json", "w")

json.dump(planets, planet_file, indent="\t")
json.dump(stars, star_file, indent="\t")
json.dump(galaxies, galaxy_file, indent="\t")
json.dump(satellites, satellite_file, indent="\t")

print("Num of Planets:", len(planets))
print("Num of Stars:", len(stars))
print("Num of Galaxies:", len(galaxies))
print("Num of Satellites:", len(satellites))
print("Done")