import urllib.request
import json
import Spacecowboy
from Spacecowboy import implode
import sys
                  
def star_scrape() :
    """
    Calls the Kepler data api and returns a set of stars
    returns a list of dictionaries that contains all attrs of the star model
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
    stars = []
    
    for web_star in web_table :
        if all(web_star.values()) :
            stars.append(translate_star(web_star))

    return filter_stars(stars)

def translate_star(web_star) :
    """
    Translates a star from the kepler data to a spacecowboy star
    """
    translators = [t_pid, t_name, t_diameter, t_ra, t_dec, t_temp, t_mass, t_img, t_galaxy]
    return dict([t(web_star) for t in translators])

pid = 0
def t_pid(web_star) :
    global pid
    pid += 1
    return ("pid", pid)

def t_name(web_star) :
    return ("name", str(web_star["pl_hostname"]))

def t_diameter(web_star) :
    diameter = Spacecowboy.sol_rad * web_star["st_rad"] * 2
    return ("diameter", float(diameter))

def t_ra(web_star) :
    return ("ra", float(web_star["ra"]))

def t_dec(web_star) :
    return ("dec", float(web_star["dec"]))

def t_temp(web_star) :
    return ("temperature", int(web_star["st_teff"]))

def t_mass(web_star) :
    return ("mass", float(web_star["st_mass"]))

def t_img(web_star) :
    return ("img_url", "star.png")

def t_galaxy(web_star) :
    return ("galaxy_pid", -1)

def filter_stars(stars) :
    """
    Filters a table of stars removing any entries that have 
    empty attrs or are not unique
    """
    stars = list(filter(lambda star : all(star.values()), stars))
    unique_stars = list({star["name"] : star for star in stars}.values())

    i = 1
    for star in unique_stars :
        star["pid"] = i
        i += 1

    return unique_stars


#################
# Execution
#################

print("Scraping stars.");
stars = star_scrape()
stars_file = open("../scraped_data/scraped_stars.json", "w")
json.dump(stars, stars_file, indent="\t")
stars_file.close()
print("Scraped " + str(len(stars)) + " stars.")