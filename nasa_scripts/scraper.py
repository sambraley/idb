from planet_scrape import planet_scrape
from star_scrape import star_scrape
from galaxy_scrape import galaxy_scrape
from satellite_scrape import satellite_scrape
import json

planets = planet_scrape()
stars = star_scrape()
galaxies = galaxy_scrape()
satellites = satellite_scrape()

# hardcode elements
earth = {"pid":1,\
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
         "star_pid":1,\
         "galaxy_pid":1 }

sun = {"pid":1,\
       "name":"Sun",\
       "diameter":1.3914 * (10 **6),\
       "image":"",\
       "ra":0.49288194,\
       "dec":3.1928926,\
       "temperature":5778,\
       "mass":1.989 * (10 ** 30),\
       "galaxy_pid":1}

milky_way = {"pid":1,\
             "name": "Milky Way",\
             "image": "",\
             "ra":17.7533,\
             "dec":-47.2833,\
             "type":"Spiral",\
             "redshift":0,\
             "size":360}

planets.insert(0,earth)
stars.insert(0, sun)
galaxies.insert(0, milky_way)

i = 2
for s in stars :
    if s["pid"] != 1 :
        s["pid"] = i
        i += 1
        s["galaxy_pid"] = 1

i = 2
for p in planets :
    if p["pid"] != 1 :
        p["pid"] = i
        star_pid = -1

        for s in stars :
            if p["hostname"] is s["name"] :
                star_pid = s["pid"]
                break
        p.pop("hostname")
        p["galaxy_pid"] = 1

i = 2
for g in galaxies :
    if g["pid"] != 1 :
        g["pid"] = i
        i += 1

i = 1
for s in satellites :
    s["host_pid"] = 1
    s["pid"] = i
    i += 1

planet_file = open("planets.json", "w")
star_file = open("stars.json", "w")
galaxy_file = open("galaxies.json", "w")
satellite_file = open("satellites.json", "w")

json.dump(planets, planet_file, indent="\t")
json.dump(stars, star_file, indent="\t")
json.dump(galaxies, galaxy_file, indent="\t")
json.dump(satellites, satellite_file, indent="\t")

print("Done")
