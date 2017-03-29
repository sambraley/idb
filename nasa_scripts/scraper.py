from planet_scrape import planet_scrape
from star_scrape import star_scrape
from galaxy_scrape import galaxy_scrape
from satellite_scrape import satellite_scrape
import json

stars = star_scrape()
planets = planet_scrape(stars)
galaxies = galaxy_scrape()
satellites = satellite_scrape()

# hardcode elements
earth = {"pid":planets[len(planets)-1]["pid"] + 1,\
         "name":"Earth",\
         "diameter":12742,\
         "image":"",\
         "ra":0,\
         "dec":0,\
         "gravity":9.81,\
         "orbital_period":365,\
         "mass":5.972 * (10 ** 24),\
         "temperature":287,\
         "host_pid":-1,\
         "star_pid":stars[len(stars)-1]["pid"] + 1,\
         "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1 }

sun = {"pid":stars[len(stars)-1]["pid"] + 1,\
       "name":"Sun",\
       "diameter":1.3914 * (10 **6),\
       "image":"",\
       "ra":0.49288194,\
       "dec":3.1928926,\
       "temperature":5778,\
       "mass":1.989 * (10 ** 30),\
       "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1}

milky_way = {"pid":galaxies[len(galaxies)-1]["pid"] + 1,\
             "name": "Milky Way",\
             "image": "",\
             "ra":17.7533,\
             "dec":-47.2833,\
             "type":"Spiral",\
             "redshift":0,\
             "size":360}

planets.append(earth)
stars.append(sun)
galaxies.append(milky_way)

for s in stars :
    s["galaxy_pid"] = milky_way["pid"]

for s in satellites :
    s["host_pid"] = earth["pid"]
    s["star_pid"] = sun["pid"]
    s["galaxy_pid"] = milky_way["pid"]

planet_file = open("planets.json", "w")
star_file = open("stars.json", "w")
galaxy_file = open("galaxies.json", "w")
satellite_file = open("satellites.json", "w")

json.dump(planets, planet_file, indent="\t")
json.dump(stars, star_file, indent="\t")
json.dump(galaxies, galaxy_file, indent="\t")
json.dump(satellites, satellite_file, indent="\t")

print("Done")
