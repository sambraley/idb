import urllib.request
import json
import sys

required_attrs = ["pl_name", "pl_radj", "pl_massj", "pl_orbper", "pl_eqt", \
                  "pl_hostname", "st_rad", "ra", "dec", "st_teff", "st_mass"]

def scrape(w) :
    raw = request_data()
    json = transform_data(raw)
    json = filter_data(json)
    write_data(w, json)

def request_data() :
    base = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?"
    table = "exoplanets"
    output_format = "json"
    
    # Build Request String
    attr_query = implode(required_attrs, ",")
    request_str = base + "table=" + table + "&select=" + attr_query + "&format=" + output_format

    raw = urllib.request.urlopen(request_str).read().decode("utf-8")
    return raw

def implode(i, delimeter) :
    imploded = "";
    for e in i :
        imploded += e + delimeter

    imploded = imploded[:-len(delimeter)]
    return imploded

def transform_data(raw) : 
    return json.loads(raw)

def filter_data(json) :
    return list(filter(lambda d : has_attrs(d, required_attrs), json))

def has_attrs (d, attrs) :
    for attr in attrs :
        if attr in d and d[attr] is None :
            return False
    return True

def write_data(w, data) :
    json.dump(data, w)
