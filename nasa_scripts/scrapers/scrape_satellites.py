import json
import urllib.request
import sys
from Spacecowboy import implode

def satellite_scrape() : 
    """
    Calls the launch library api and returns a set of satellites
    returns a list of dictionaries that contains all attrs of the satellite model
    """
    url_fields = ["limit=800",
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
    translators = [t_pid, t_name, t_image, t_year, t_agency, t_info, t_type, t_ppid, t_spid, t_gpid]
    return dict([t(web_sat) for t in translators])

pid = 0
def t_pid(web_sat) :
    global pid
    pid += 1
    return ("pid", pid)
    
def t_name(web_sat) : 
    return ("name", str(web_sat["name"]))

def t_image(web_sat) : 
    return ("img_url", "satellite.png")

def t_year(web_sat) : 
    return ("year_launched", int(web_sat["launch"]["windowstart"].split(" ")[2]))

def t_agency(web_sat) : 
    return ("agency", str(web_sat["agencies"][0]["name"]))

def t_info(web_sat) :
    return ("info_url", str(web_sat["wikiURL"]))

def t_type(web_sat) : 
    return ("mission_type", str(web_sat["typeName"]))

def t_ppid(web_sat) : 
    return ("planet_pid", -1)

def t_spid(web_sat) : 
    return ("star_pid", -1)

def t_gpid(web_sat) : 
    return ("galaxy_pid", -1)
    

def filter_sats(sats) : 
    def correct_mission(sat) :
        correct = sat["mission_type"] == "Earth Science"
        correct = correct or sat["mission_type"] == "Planetary Science"
        correct = correct or sat["mission_type"] == "Heliophysics"
        return correct
        
    sats = list(filter(lambda sat : all(sat.values()) and correct_mission(sat), sats))
    
    i = 1
    for sat in sats :
        sat["pid"] = i
        i += 1
    
    return sats
    
def satellite_image_scrape(satellites):
    url_fields = ["action=query","format=json"]
    url_base = "https://en.wikipedia.org/w/api.php?"
	
    satellite_img_urls = dict()
    for satellite in satellites:
        name = satellite["name"]
        satellite_img_urls[name] = [] 
        search_fields = {'action': 'query', 'format': 'json', 'list':'search', 'srsearch':name + "-Satellite"}

        url_str = url_base + urllib.parse.urlencode(search_fields)

        raw = urllib.request.urlopen(url_str).read().decode("utf-8")

        wiki_json = json.loads(raw)["query"]["search"]
        if len(wiki_json) != 0 :
            wiki_title = json.loads(raw)["query"]["search"][0]["title"]

            img_search_fields = {'action': 'query', 'format': 'json', 'prop':'images', 'titles':wiki_title}

            url_str = url_base + urllib.parse.urlencode(img_search_fields)

            raw = urllib.request.urlopen(url_str).read().decode("utf-8")

            pages = json.loads(raw)["query"]["pages"]

            for page in pages.values():
                if "images" in page:
                    #not all satellites have images
                    first_image = True;
                    for img in page["images"]:
                        img_title = img["title"]
                        img_info_fields = {'action': 'query', 'format': 'json', 'titles':img_title, 'prop':'imageinfo', 'iiprop': 'url'}
                        url_str = url_base + urllib.parse.urlencode(img_info_fields)
                        raw = urllib.request.urlopen(url_str).read().decode("utf-8")

                        url = next(iter(json.loads(raw)["query"]["pages"].values()))["imageinfo"][0]["url"]

                        satellite_img_urls[name].append({"title" : img_title, "url": url})

                        if first_image :
                            satellite["img_url"] = url
                            first_image = False

    return satellites


#################
# Execution
#################

print("Scraping satellites.");
satellites = satellite_scrape()
satellites = satellite_image_scrape(satellites)
satellites_file = open("../scraped_data/scraped_satellites.json", "w")
json.dump(satellites, satellites_file, indent="\t")
satellites_file.close()
print("Scraped " + str(len(satellites)) + " satellites.")
