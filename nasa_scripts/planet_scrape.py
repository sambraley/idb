import urllib.request
import json
import sys
import Spacecowboy
from Spacecowboy import implode

def planet_scrape(stars) :
    """
    Calls the kepler data api and returns a set of planets
    returns a list of dictionaries of the spacecowboy planet model
    stars a list of stars to connect the planets to
    """
    web_table_attrs = ["pl_name", 
                   "pl_radj", 
                   "pl_massj",
                   "pl_orbper", 
                   "pl_eqt",
                   "pl_hostname",
                   "st_rad", 
                   "ra", 
                   "dec", 
                   "st_teff", 
                   "st_mass", 
                   "st_rad"]

    url_fields = ["table=exoplanets",
                  "format=json",
                  "select=" + implode(web_table_attrs, ",")]

    url_base = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?"
    
    web_table = request_data(url_base + implode(url_fields, "&"))
    spacecowboy_table = translate_table(web_table, stars)

    return spacecowboy_table


def request_data(url_str) :
    raw = urllib.request.urlopen(url_str).read().decode("utf-8")
    return json.loads(raw)
    
#####################
# Translators
#####################
def translate_table(web_table, stars) :
    """
    Given a table from the kepler data, translates the table
    into a table for spacecowboys
    """
    planets = []
    for web_planet in web_table :
        if all(web_planet.values()) :
            planets.append(translate_planet(web_planet, stars))

    return filter_planets(planets)

def translate_planet(web_planet, stars) :
    """
    Translates a planet from the kepler data to a spacecowboy planet
    """
    translators = [t_pid, t_name, t_diameter, t_ra, t_dec, t_gravity, t_op, t_temp, t_img, t_mass, t_spid, t_gpid]
    return dict([t(web_planet, stars) for t in translators])

pid = 0
def t_pid(web_planet, stars) :
    global pid
    pid += 1
    return ("pid", pid)

def t_name(web_planet, stars) : 
    return ("name", str(web_planet["pl_name"]))

def t_diameter(web_planet, stars) : 
    diameter = 2 * web_planet["pl_radj"] * Spacecowboy.radj
    return ("diameter", float(diameter))

def t_ra(web_planet, stars) : 
    return ("ra", float(web_planet["ra"]))

def t_dec(web_planet, stars) : 
    return ("dec", float(web_planet["dec"]))

def t_gravity(web_planet, stars) : 
    mass = web_planet["pl_massj"] * Spacecowboy.massj
    radius = web_planet["pl_radj"] * Spacecowboy.radj
    gravity = (Spacecowboy.G * mass) / (radius ** 2)
    return ("gravity", float(gravity))

def t_op(web_planet, stars) : 
    return ("orbital_period", float(web_planet["pl_orbper"]))

def t_mass(web_planet, stars) : 
    mass = web_planet["pl_massj"] * Spacecowboy.massj
    return ("mass", float(mass))

def t_temp(web_planet, stars) : 
    return ("temperature", int(web_planet["pl_eqt"]))

def t_img(web_planet, stars) :
    return ("img_url", "planet.png")

def t_spid(web_planet, stars) : 
    spid = -1
    for star in stars :
      if star["name"] == web_planet["pl_hostname"] :
          spid = star["pid"]
          break
            
    return ("star_pid", spid)

def t_gpid(web_planet, stars) : 
    return ("galaxy_pid", -1)


def filter_planets(planets) :
    planets = list(filter(lambda p : all(p.values()), planets))
    
    i = 1
    for p in planets :
        p["pid"] = i
        i += 1
        
    return planets
