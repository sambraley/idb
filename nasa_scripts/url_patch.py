import json

planets = json.load(open("scraped_data/scraped_planets.json"))
galaxies = json.load(open("scraped_data/scraped_galaxies.json"))
stars = json.load(open("scraped_data/scraped_stars.json"))
satellites = json.load(open("scraped_data/scraped_satellites.json"))

# Create Image url
images = []
planet_urls_file = open("imgs/compiled_planets_imgs.json", "r")
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
  images += [{"url":url,"name":s["name"]}]
  
num = 1
for i in images:
    url = i["url"]
    i.pop("url")
    pid = num
    num += 1
    i["pid"] = pid
    i["img_url"] = url

print("Patching data together with pids.")

# hardcode elements
jupiter_image = {
    "pid":images[len(images)-1]["pid"] + 1,
    "img_url":"https://upload.wikimedia.org/wikipedia/commons/2/2b/Jupiter_and_its_shrunken_Great_Red_Spot.jpg"
    }

earth_image = {
    "pid":images[len(images)-1]["pid"] + 2,
    "img_url":"https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg"
    }

sun_image = {
    "pid":images[len(images)-1]["pid"] + 3,
    "img_url":"http://nineplanets.org/images/thesun.jpg"
    }

mw_image = {
    "pid":images[len(images)-1]["pid"] + 4,
    "img_url":"https://apod.nasa.gov/apod/image/0801/16500feetmilkywaykc2_brunier.jpg"
    }

mercury_image = {
    "pid":images[len(images)-1]["pid"] + 5,
    "img_url": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Mercury_in_color_-_Prockter07-edit1.jpg"
    }

venus_image = {
    "pid": images[len(images)-1]["pid"] + 6,
    "img_url": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg"
    }
    
mars_image = {
    "pid":images[len(images)-1]["pid"] + 7,
    "img_url": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg"
    }
    
saturn_image = {
    "pid":images[len(images)-1]["pid"] + 8,
    "img_url": "http://spaceaim.com/wp-content/uploads/2015/07/Saturn.png"
    }
    
uranus_image = {
    "pid":images[len(images)-1]["pid"] + 9,
    "img_url": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg"
    }
    
neptune_image = {
    "pid":images[len(images)-1]["pid"] + 10,
    "img_url":"https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg"
    }
    
pluto_image = {
    "pid":images[len(images)-1]["pid"] + 11,
    "img_url":"https://upload.wikimedia.org/wikipedia/commons/2/2a/Nh-pluto-in-true-color_2x_JPEG-edit-frame.jpg"
    }

maven_image = {
    "pid":images[len(images)-1]["pid"] + 12,
    "img_url": "https://upload.wikimedia.org/wikipedia/commons/a/ac/MAVEN_Transparent.png"
    }
    
juno_image = {
    "pid":images[len(images)-1]["pid"] + 13,
    "img_url":"https://upload.wikimedia.org/wikipedia/commons/5/51/Juno_Transparent.png"
    }

milky_way = {
    "pid":galaxies[len(galaxies)-1]["pid"] + 1,
    "name": "Milky Way",
    "ra":17.7533,
    "dec":-47.2833,
    "morph_type":"Spiral",
    "redshift":0.0,
    "size":360.0,
    "image_pid":mw_image["pid"]
    }
            
            
sun =   {
    "pid":stars[len(stars)-1]["pid"] + 1,
    "name":"Sun",
    "diameter":1.0,
    "ra":23.1458,
    "dec":9.6697,
    "temperature":5778,
    "mass":1.0,
    "galaxy_pid":galaxies[len(galaxies)-1]["pid"] + 1,
    "image_pid":sun_image["pid"]
    }

jupiter_mass_kg = 1.898 * (10 ** 27)
jupiter_radius_km = 69911
jupiter = {
    "pid":planets[len(planets)-1]["pid"] + 1,
    "name":"Jupiter",
    "diameter":float(1),
    "ra":196.0167,
    "dec":-5.1181,
    "gravity":float(1),
    "orbital_period":float(4380),
    "mass":float(1),
    "temperature":128,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":jupiter_image["pid"]
    }

earth_mass_kg = 5.972 * (10 ** 24)
earth_radius_km = 6371
earth = {
    "pid":planets[len(planets)-1]["pid"] + 2,
    "name":"Earth",
    "diameter":float((earth_radius_km * 2)) / (jupiter_radius_km * 2),
    "ra":0.0,
    "dec":0.0,
    "gravity":float((earth_mass_kg / jupiter_mass_kg)) / ((earth_radius_km / jupiter_radius_km) ** 2),
    "orbital_period":float(365),
    "mass":float(earth_mass_kg) / jupiter_mass_kg,
    "temperature":287,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":earth_image["pid"]
    }

mercury_mass_kg = 3.285 * (10 ** 23)
mercury_radius_km = 2440
mercury = {
    "pid":planets[len(planets)-1]["pid"] + 3,
    "name":"Mercury",
    "diameter":float((mercury_radius_km * 2)) / (jupiter_radius_km * 2),
    "ra":28.6958,
    "dec":14.0792,
    "gravity":float((mercury_mass_kg / jupiter_mass_kg)) / ((mercury_radius_km / jupiter_radius_km) ** 2),
    "orbital_period":float(88),
    "mass":float(mercury_mass_kg) / jupiter_mass_kg,
    "temperature":440,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":mercury_image["pid"]
    }
    
venus_mass_kg = 4.867 * (10 ** 24)
venus_radius_km = 6052
venus = {
    "pid":planets[len(planets)-1]["pid"] + 4,
    "name":"Venus",
    "diameter":float((venus_radius_km * 2)) / (jupiter_radius_km * 2),
    "ra":355.5375,
    "dec":2.2594,
    "gravity":float((venus_mass_kg / jupiter_mass_kg)) / ((venus_radius_km / jupiter_radius_km) ** 2),
    "orbital_period":float(225),
    "mass":float(venus_mass_kg) / jupiter_mass_kg,
    "temperature":735,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":venus_image["pid"]
    }
    
mars_mass_kg = 6.39 * (10 ** 23)
mars_radius_km = 3390
mars = {
    "pid":planets[len(planets)-1]["pid"] + 5,
    "name":"Mars",
    "diameter":float((mars_radius_km * 2)) / (jupiter_radius_km * 2),
    "ra":50.9625,
    "dec":20.1067,
    "gravity":float((mars_mass_kg / jupiter_mass_kg)) / ((mars_radius_km / jupiter_radius_km) ** 2),
    "orbital_period":float(687),
    "mass":float(mars_mass_kg) / jupiter_mass_kg,
    "temperature":213,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":mars_image["pid"]
    }
    
saturn_mass_kg = 5.683 * (10 ** 26)
saturn_radius_km = 58232
saturn = {
    "pid":planets[len(planets)-1]["pid"] + 6,
    "name":"Saturn",
    "diameter":float((saturn_radius_km * 2)) / (jupiter_radius_km * 2),
    "ra":267.2333,
    "dec":-22.0558,
    "gravity":float((saturn_mass_kg / jupiter_mass_kg)) / ((saturn_radius_km / jupiter_radius_km) ** 2),
    "orbital_period":float(10585),
    "mass":float(saturn_mass_kg) / jupiter_mass_kg,
    "temperature":95,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":saturn_image["pid"]
    }
    
uranus_mass_kg = 8.681 * (10 ** 25)
uranus_radius_km = 25362
uranus = {
    "pid":planets[len(planets)-1]["pid"] + 7,
    "name":"Uranus",
    "diameter":float((uranus_radius_km * 2)) / (jupiter_radius_km * 2),
    "ra":22.8417,
    "dec":8.9517,
    "gravity":float((uranus_mass_kg / jupiter_mass_kg)) / ((uranus_radius_km / jupiter_radius_km) ** 2),
    "orbital_period":float(30660),
    "mass":float(uranus_mass_kg) / jupiter_mass_kg,
    "temperature":76,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":uranus_image["pid"]
    }
    
neptune_mass_kg = 1.024 * (10 ** 26)
neptune_radius_km = 24622
neptune = {
    "pid":planets[len(planets)-1]["pid"] + 8,
    "name":"Neptune",
    "diameter":float((neptune_radius_km * 2)) / (jupiter_radius_km * 2),
    "ra":344.7625,
    "dec":-7.4342,
    "gravity":float((neptune_mass_kg / jupiter_mass_kg)) / ((neptune_radius_km / jupiter_radius_km) ** 2),
    "orbital_period":float(60225),
    "mass":float(neptune_mass_kg) / jupiter_mass_kg,
    "temperature":59,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":neptune_image["pid"]
    }
    
pluto_mass_kg = 1.309 * (10 ** 22)
pluto_radius_km = 1187
pluto = {
    "pid":planets[len(planets)-1]["pid"] + 9,
    "name":"Pluto",
    "diameter":float((pluto_radius_km * 2)) / (jupiter_radius_km * 2),
    "ra":290.600,
    "dec":-21.1981,
    "gravity":float((pluto_mass_kg / jupiter_mass_kg)) / ((pluto_radius_km / jupiter_radius_km) ** 2),
    "orbital_period":float(90520),
    "mass":float(pluto_mass_kg) / jupiter_mass_kg,
    "temperature":44,
    "star_pid":sun["pid"],
    "galaxy_pid":milky_way["pid"],
    "image_pid":pluto_image["pid"]
    }
    
maven = {
    "planet_pid": mars["pid"],
    "pid": satellites[len(satellites)-1]["pid"] + 1,
    "galaxy_pid": milky_way["pid"],
    "agency": "National Aeronautics and Space Administration",
    "name": "MAVEN",
    "year_launched": 2013,
    "info_url": "https://en.wikipedia.org/wiki/MAVEN",
    "mission_type": "Planetary Science",
    "image_pid":maven_image["pid"],
    "star_pid": sun["pid"]
	}

juno = {
    "planet_pid": jupiter["pid"],
    "pid": satellites[len(satellites)-1]["pid"] + 2,
    "galaxy_pid": milky_way["pid"],
    "agency": "National Aeronautics and Space Administration",
    "name": "Juno",
    "year_launched": 2011,
    "info_url": "https://en.wikipedia.org/wiki/Juno_(spacecraft)",
    "mission_type": "Planetary Science",
    "image_pid":juno_image["pid"],
    "star_pid": sun["pid"]
	}

for p in planets :
    p["galaxy_pid"] = milky_way["pid"]
    hostname = p.pop("hostname")

    star_pid = -1;

    for s in stars :
        if s["name"] == hostname :
            star_pid = s["pid"]
            break

    p["star_pid"] = star_pid;

    img_pid = -1
    for i in images:
        if "ra" in i:
            if i["ra"] == p["ra"] and i["dec"] == p["dec"] :
                img_pid = i["pid"]
                break
    
    p["image_pid"] = img_pid
    
    if "img_url" in p:
        p.pop("img_url")
    
for g in galaxies:
    img_pid = -1
    for i in images:
        if "ra" in i:
            if i["ra"] == g["ra"] and i["dec"] == g["dec"] :
                img_pid = i["pid"]
                break
    
    g["image_pid"] = img_pid
    
    if "img_url" in g:
        g.pop("img_url")

for s in stars :
    s["galaxy_pid"] = milky_way["pid"]
    img_pid = -1
    for i in images:
        if "ra" in i:
            if i["ra"] == s["ra"] and i["dec"] == s["dec"] :
                img_pid = i["pid"]
                break
    
    s["image_pid"] = img_pid
    
    if "img_url" in s:
        s.pop("img_url")
    
for s in satellites :
    s["planet_pid"] = earth["pid"]
    s["star_pid"] = sun["pid"]
    s["galaxy_pid"] = milky_way["pid"]
    
    img_pid = -1
    for i in images:
        if "name" in i:
            if i["name"] == s["name"] :
              img_pid = i["pid"]
              break
    
    s["image_pid"] = img_pid
    
    if "img_url" in s:
        s.pop("img_url")
        
for i in images:
    if "ra" in i:
        i.pop("ra")
        i.pop("dec")
        
    if "name" in i:
        i.pop("name")
    
print("Adding hardcoded elements.")

satellites.append(maven)
satellites.append(juno)

planets.append(jupiter)
planets.append(earth)
planets.append(mercury)
planets.append(venus)
planets.append(mars)
planets.append(saturn)
planets.append(uranus)
planets.append(neptune)
planets.append(pluto)

stars.append(sun)

galaxies.append(milky_way)

images.append(jupiter_image)
images.append(earth_image)
images.append(sun_image)
images.append(mw_image)
images.append(mercury_image)
images.append(venus_image)
images.append(mars_image)
images.append(saturn_image)
images.append(uranus_image)
images.append(neptune_image)
images.append(pluto_image)
images.append(maven_image)
images.append(juno_image)

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