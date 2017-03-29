import urllib.request
import json
import sys

required_attrs = ["pl_name", "pl_radj", "pl_massj", "pl_orbper", "pl_eqt", \
                  "pl_hostname", "st_rad", "ra", "dec", "st_teff", "st_mass", "st_rad"]
                  
def star_scrape() : 
    json = request_data()
    json = filter_data(json)
    json = transform_data(json)
    return json

def request_data() :
    base = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?"
    table = "exoplanets"
    output_format = "json"
    
    # Build Request String
    attr_query = implode(required_attrs, ",")
    request_str = base + "table=" + table + "&select=" + attr_query + "&format=" + output_format

    raw = urllib.request.urlopen(request_str).read().decode("utf-8")
    return json.loads(raw)

def implode(i, delimeter) :
    imploded = "";
    for e in i :
        imploded += e + delimeter

    imploded = imploded[:-len(delimeter)]
    return imploded

def transform_data(json) :
    sol_rad = 695700

    stars = []
    for d in json :
        star = {}
        star["pid"] = -1
        star["name"] = d["pl_hostname"]
        star["diameter"] = sol_rad * d["st_rad"] * 2
        star["image"] = ""
        star["ra"] = d["ra"]
        star["dec"] = d["dec"]
        star["temperature"] = d["st_teff"]
        star["mass"] = d["st_mass"]
        star["galaxy_pid"] = -1
        stars.append(star)

    return stars

def filter_data(json) :
    data = list(filter(lambda d : has_attrs(d, required_attrs), json))
    unique_data = list({d["pl_hostname"] : d for d in data}.values())
    return unique_data

def has_attrs(d, attrs) :
    for attr in attrs :
        if attr not in d or d[attr] is None :
            return False
    return True

