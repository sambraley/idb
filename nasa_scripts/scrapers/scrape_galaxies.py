import json
import urllib.request
import sys
from Spacecowboy import implode

def galaxy_scrape() :
    web_table_search = ["otype=%27G%27"]
    
    url_fields = ["OutputMode=LIST",
                  "maxObject=1000",
                  "Criteria=" + implode(web_table_search, " & "),
                  "output.format=ASCII",
                  "list.otypesel=on",
                  "otypedisp=3",
                  "list.coo1=on",
                  "frame1=ICRS",
                  "coodisp1=d2",
                  "list.rvsel=on",
                  "rvDisplay=Z",
                  "list.mtsel=on",
                  "list.sizesel=on",
                  "list.fluxsel=off",
                  "list.bibsel=off",
                  "list.notesel=off",
                  "list.spsel=off"]
                  
    url_base = "http://simbad.u-strasbg.fr/simbad/sim-sam?"
    web_table = request_data(url_base + implode(url_fields, "&"))
    spacecowboy_table = translate_table(web_table)
    return spacecowboy_table

def request_data(url_str) : 
    raw = urllib.request.urlopen(url_str).read().decode("utf-8")
    return ascii_to_json(raw)
    
def ascii_to_json(ascii_data) :
    # skip titles etc.
    i = iter(ascii_data.splitlines())
    for _ in range(0, 7) :
        next(i)
    
    # get table attr names and skip next line
    keys = [key.strip() for key in next(i).split("|")]
    next(i)

    # turn data into json form
    data = []
    for line in i :
        if "|" in line :
            values = [value.replace("~", "").strip() for value in line.split("|")]
            datum = {t[0]:t[1] for t in zip(keys, values)}
            data.append(datum)
    return data
    
def translate_table(web_table) :
    """
    Given a table from the simbad data, translates the table
    into a table for spacecowboys
    """
    galaxies = []
    for web_galaxy in web_table :
        if all(web_galaxy.values()) :
            galaxies.append(translate_galaxy(web_galaxy))

    return filter_galaxies(galaxies)

def translate_galaxy(web_galaxy) :
    """
    Translates a galaxy from the simbad data to a spacecowboy galaxy
    """
    translators = [t_pid, t_name, t_ra, t_dec, t_type, t_redshift, t_size, t_img]
    return dict([t(web_galaxy) for t in translators])

pid = 0
def t_pid(web_galaxy) : 
    global pid
    pid += 1
    return ("pid",pid)
    
def t_name(web_galaxy) : 
    return ("name", str(web_galaxy["identifier"]))

def t_ra(web_galaxy) : 
    return ("ra", float(web_galaxy["coord1 (ICRS,J2000/2000)"].split(" ")[0]))

def t_dec(web_galaxy) : 
    return ("dec", float(web_galaxy["coord1 (ICRS,J2000/2000)"].split(" ")[1]))

def t_type(web_galaxy) : 
    morph_type = ""
    
    if "SB" in web_galaxy["morph. type"] :
        morph_type = "Barred Spiral"
    elif "S" in web_galaxy["morph. type"] :
        morph_type = "Spiral"
    elif "I" in web_galaxy["morph. type"] :
        morph_type = "Irregular"
    elif "E" in web_galaxy["morph. type"] :
        morph_type = "Elliptical"
    return ("morph_type", morph_type)
    
def t_redshift(web_galaxy) : 
    return ("redshift", float(web_galaxy["redshift"]))

def t_size(web_galaxy) : 
    return ("size", float(web_galaxy["ang. size"].split(" ")[0]))

def t_img(web_galaxy) :
    return ("img_url", "galaxy.png")

def filter_galaxies(galaxies) : 
    galaxies = list(filter(lambda galaxy : all(galaxy.values()), galaxies))

    i = 1
    for galaxy in galaxies :
        galaxy["pid"] = i
        i += 1
        
    return galaxies

    
###############
# Execution
###############
print("Scraping galaxies.");
galaxies = galaxy_scrape()
galaxies_file = open("../scraped_data/scraped_galaxies.json", "w")
json.dump(galaxies, galaxies_file, indent="\t")
galaxies_file.close()
print("Scraped " + str(len(galaxies)) + " galaxies.")

