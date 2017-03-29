import urllib.request
import json
import sys

required_attrs = ["pl_name", "pl_radj", "pl_massj", "pl_orbper", "pl_eqt", \
                  "pl_hostname", "st_rad", "ra", "dec", "st_teff", "st_mass", "st_rad"]

def planet_scrape() :
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
    radj = 69911
    G = 6.67408 * (10 ** -20)
    massj = 1.898 * (10 ** 27)

    planets = []
    for d in json :
        planet = {}
        planet["pid"] = -1
        planet["name"] = d["pl_name"]
        planet["diameter"] = 2 * d["pl_radj"] * radj
        planet["image"] = ""
        planet["ra"] = d["ra"]
        planet["dec"] = d["dec"]
        planet["gravity"] = (G * d["pl_massj"] * massj) / (( d["pl_radj"] * radj) ** 2)
        planet["orbital_period"] = d["pl_orbper"]
        planet["mass"] = d["pl_massj"] * massj
        planet["temperature"] = d["pl_eqt"]
        planet["hostname"] = d["pl_hostname"]
        planet["host_pid"] = -1
        planet["star_pid"] = -1
        planet["galaxy_pid"] = -1

        planets.append(planet)

    return planets


def filter_data(json) :
    return list(filter(lambda d : has_attrs(d, required_attrs), json))

def has_attrs (d, attrs) :
    for attr in attrs :
        if attr not in d or d[attr] is None :
            return False
    return True

