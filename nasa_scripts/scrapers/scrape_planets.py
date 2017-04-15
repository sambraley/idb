import urllib.request
import json
import sys
import Spacecowboy
from Spacecowboy import implode

def planet_scrape() :
    """
    Calls the kepler data api and returns a set of planets
    returns a list of dictionaries of the spacecowboy planet model
    """
    web_table_attrs = ["pl_name", 
                   "pl_radj", 
                   "pl_massj",
                   "pl_orbper", 
                   "pl_eqt",
                   "pl_hostname",
                   "st_rad", 
                   "ra", 
                   "dec"]

    url_fields = ["table=exoplanets",
                  "format=json",
                  "select=" + implode(web_table_attrs, ",")]

    url_base = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?"
    
    web_table = request_data(url_base + implode(url_fields, "&"))
    spacecowboy_table = translate_table(web_table)

    return spacecowboy_table


def request_data(url_str) :
    raw = urllib.request.urlopen(url_str).read().decode("utf-8")
    return json.loads(raw)
    
#####################
# Translators
#####################
def translate_table(web_table) :
    """
    Given a table from the kepler data, translates the table
    into a table for spacecowboys
    """
    planets = []
    for web_planet in web_table :
        if all(web_planet.values()) :
            planets.append(translate_planet(web_planet))

    return filter_planets(planets)

def translate_planet(web_planet) :
    """
    Translates a planet from the kepler data to a spacecowboy planet
    """
    translators = [t_pid, t_name, t_diameter, t_ra, t_dec, t_gravity, t_op, t_temp, t_img, t_mass, t_spid, t_gpid, t_hostname]
    return dict([t(web_planet) for t in translators])

pid = 0
def t_pid(web_planet) :
    global pid
    pid += 1
    return ("pid", pid)

def t_name(web_planet) : 
    return ("name", str(web_planet["pl_name"]))

def t_diameter(web_planet) : 
    diameter = 2 * web_planet["pl_radj"]
    return ("diameter", float(diameter))

def t_ra(web_planet) : 
    return ("ra", float(web_planet["ra"]))

def t_dec(web_planet) : 
    return ("dec", float(web_planet["dec"]))

def t_gravity(web_planet) : 
    mass = web_planet["pl_massj"]
    radius = web_planet["pl_radj"]
    gravity = mass / (radius ** 2)
    return ("gravity", float(gravity))

def t_op(web_planet) : 
    return ("orbital_period", float(web_planet["pl_orbper"]))

def t_mass(web_planet) : 
    mass = web_planet["pl_massj"]
    return ("mass", float(mass))

def t_temp(web_planet) : 
    return ("temperature", int(web_planet["pl_eqt"]))

def t_img(web_planet) :
    return ("img_url", "planet.png")

def t_spid(web_planet) : 
    return ("star_pid", -1)

def t_gpid(web_planet) : 
    return ("galaxy_pid", -1)

def t_hostname(web_planet) :
		return ("hostname", web_planet["pl_hostname"])


def filter_planets(planets) :
    planets = list(filter(lambda p : all(p.values()), planets))
    
    i = 1
    for p in planets :
        p["pid"] = i
        i += 1
        
    return planets


#################
# Execution
#################

print("Scraping planets.");
planets = planet_scrape()
planets_file = open("../scraped_data/scraped_planets.json", "w")
json.dump(planets, planets_file, indent="\t")
planets_file.close()
print("Scraped " + str(len(planets)) + " planets.")