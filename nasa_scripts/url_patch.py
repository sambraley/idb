import json

planets = json.load(open("scraped_data/scraped_planets.json"))
galaxies = json.load(open("scraped_data/scraped_galaxies.json"))
stars = json.load(open("scraped_data/scraped_stars.json"))
satellites = json.load(open("scraped_data/scraped_satellites.json"))

# Create Image url
images = []
planet_urls_file = open("imgs/compiled_planet_imgs.json", "r")
images += json.load(planet_urls_file)
planet_urls_file.close()

galaxies_urls_file = open("imgs/compiled_galaxies_imgs.json", "r")
images += json.load(galaxies_urls_file)
galaxies_urls_file.close()

stars_urls_file = open("imgs/compiled_stars_imgs.json", "r")
images += json.load(stars_urls_file)
stars_urls_file.close()

for s in satellites:
  url = s["img_url"]
  pid = -1
  images += [{"url":url,"pid":pid}]
  
num = 1
for i in images:
    url = i["url"]
    i.pop("url")
    pid = num
    num += 1
    i["pid"] = pid
    i["img_url"] = url

print("Adding hardcoded elements.")

# hardcode elements
earth_image = {"pid":images[len(images)-1]["pid"] + 1,
               "img_url":"https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg"}
sun_image = {"pid":images[len(images)-1]["pid"] + 2,
               "img_url":"http://nineplanets.org/images/thesun.jpg"}
mw_image = {"pid":images[len(images)-1]["pid"] + 3,
            "img_url":"https://apod.nasa.gov/apod/image/0801/16500feetmilkywaykc2_brunier.jpg"}
               
earth = {"pid":planets[len(planets)-1]["pid"] + 1,
         "name":"Earth",
         "diameter":float(12742),
         "ra":0.0,
         "dec":0.0,
         "gravity":9.81,
         "orbital_period":float(365),
         "mass":float(5.972 * (10 ** 24)),
         "temperature":287,
         "star_pid":stars[len(stars)-1]["pid"] + 1,
         "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1,
         "image_pid":earth_image["pid"]}

sun = {"pid":stars[len(stars)-1]["pid"] + 1,
       "name":"Sun",
       "diameter":1.3914 * (10 **6),
       "ra":0.49288194,
       "dec":3.1928926,
       "temperature":5778,
       "mass":1.0,
       "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1,
       "image_pid":sun_image["pid"]}

milky_way = {"pid":galaxies[len(galaxies)-1]["pid"] + 1,
             "name": "Milky Way",
             "ra":17.7533,
             "dec":-47.2833,
             "morph_type":"Spiral",
             "redshift":0.0,
             "size":360.0,
             "image_pid":mw_image["pid"]}

planets.append(earth)
stars.append(sun)
galaxies.append(milky_way)
images.append(earth_image)
images.append(sun_image)
images.append(mw_image)

print("Patching data together with pids.")

num = 1
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
    p["image_pid"] = num
    num += 1
    
    if "img_url" in p:
        p.pop("img_url")
    
for g in galaxies:
    g["image_pid"] = num
    num+=1
    
    if "img_url" in g:
        g.pop("img_url")

for s in stars :
    s["galaxy_pid"] = milky_way["pid"]
    s["image_pid"] = num
    num+=1
    
    if "img_url" in s:
        s.pop("img_url")
    
for s in satellites :
    s["planet_pid"] = earth["pid"]
    s["star_pid"] = sun["pid"]
    s["galaxy_pid"] = milky_way["pid"]
    s["image_pid"] = num
    num+=1
    
    if "img_url" in s:
        s.pop("img_url")


planet_file = open("data/planets.json", "w")
star_file = open("data/stars.json", "w")
galaxy_file = open("data/galaxies.json", "w")
satellite_file = open("data/satellites.json", "w")
image_file = open("data/images.json", "w")

json.dump(planets, planet_file, indent="\t")
json.dump(stars, star_file, indent="\t")
json.dump(galaxies, galaxy_file, indent="\t")
json.dump(satellites, satellite_file, indent="\t")
json.dump(images, image_file, indent="\t")

print("Num of Planets:", len(planets))
print("Num of Stars:", len(stars))
print("Num of Galaxies:", len(galaxies))
print("Num of Satellites:", len(satellites))
print("Num of Images:", len(images), " ?= ", len(planets) + len(stars) + len(galaxies) + len(satellites))
print("Done")