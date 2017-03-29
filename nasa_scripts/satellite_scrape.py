import json
import urllib.request
import sys
from Spacecowboy import implode

def satellite_scrape() : 
    """
    Calls the launch library api and returns a set of satellites
    returns a list of dictionaries that contains all attrs of the satellite model
    """
    url_fields = ["limit=100",
                  "offset=1"]
    
    url_base = "https://launchlibrary.net/1.2/mission"
    web_table = request_data(url_base + "?" + implode(url_fields, "&"), url_base)
    
    spacecowboy_table = translate_table(web_table)
    
    return spacecowboy_table
    
def request_data(url_str, url_base) : 
    raw = urllib.request.urlopen(url_str).read().decode("utf-8")
    mission_list = json.loads(raw)["missions"]
    missions = []

    for e in mission_list :
        url_str = url_base + "/" + str(e["id"])
        raw = urllib.request.urlopen(url_str).read().decode("utf-8")
        mission = json.loads(raw)["missions"][0]
        mission.pop("events")
        mission.pop("description")
        mission.pop("infoURL")
        mission.pop("wikiURL")
        mission.pop("infoURLs")
        missions.append(mission)

    return missions
    
def translate_table(web_table) :
    """
    Given a table from the launch library data, translates the table
    into a table for spacecowboys
    """
    satellites = []
    
    for web_sat in web_table :
        if all(web_sat.values()) :
            satellites.append(translate_sat(web_sat))
    return filter_sats(satellites)

def translate_sat(web_sat) :
    """
    Translates a satellite from the launch data to a spacecowboy satellite
    """
    translators = [t_pid, t_name, t_image, t_year, t_agency, t_type, t_hpid, t_spid, t_gpid]
    return dict([t(web_sat) for t in translators])

pid = 0
def t_pid(web_sat) :
    global pid
    pid += 1
    return ("pid", pid)
    
def t_name(web_sat) : 
    return ("name",web_sat["name"])

def t_image(web_sat) : 
    return ("image","satellite.png")

def t_year(web_sat) : 
    return ("year_launched", web_sat["launch"]["windowstart"].split(" ")[2])

def t_agency(web_sat) : 
    return ("agency", web_sat["agencies"][0]["name"])

def t_type(web_sat) : 
    return ("type", web_sat["typeName"])

def t_hpid(web_sat) : 
    return ("host_pid", -1)

def t_spid(web_sat) : 
    return ("star_pid", -1)

def t_gpid(web_sat) : 
    return ("galaxy_pid", -1)
    

def filter_sats(sats) : 
    sats = list(filter(lambda sat : all(sat.values()) and sat["type"] != "Human Exploration" and sat["type"] != "Resupply" and sat["type"] != "Communications", sats))
    
    i = 1
    for sat in sats :
        sat["pid"] = i
        i += 1
    
    return sats



