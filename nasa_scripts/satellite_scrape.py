import json
import urllib.request
import sys

def satellite_scrape() : 
    data = request_data()
    data = filter_data(data)
    data = transform_data(data)
    return data

def request_data() : 
    base = "https://launchlibrary.net/1.2/mission"
    limit = "limit=100"
    offset = "offset=1"
    request_str = base + "?" + implode([limit, offset], "&")

    raw = urllib.request.urlopen(request_str).read().decode("utf-8")
    mission_list = json.loads(raw)["missions"]
    missions = []

    for e in mission_list :
        request_str = base + "/" + str(e["id"])
        raw = urllib.request.urlopen(request_str).read().decode("utf-8")
        mission = json.loads(raw)["missions"][0]
        missions.append(mission)

    return missions

def implode(i, delimeter) :
    imploded = "";
    for e in i :
        imploded += e + delimeter

    imploded = imploded[:-len(delimeter)]
    return imploded


def filter_data(data) : 
    attrs = ["name", "launch", "typeName", "agencies"]
    data = list({attr:d[attr] for attr in attrs} for d in data)
    data = list(filter(lambda d : has_attrs(d, attrs), data))
    
    for d in data :
        d["year_launched"] = d["launch"]["windowstart"].split(" ")[2]
        d.pop("launch", None)
        d["agency"] = d["agencies"][0]["name"]
        d.pop("agencies", None)

    return data

def has_attrs(d, attrs) :
    for attr in attrs :
        if attr not in d or not d[attr] :
            return False
    return True

def transform_data(d) : 
    satellites = []

    for e in d :
        satellite = {}
        satellite["pid"] = -1
        satellite["name"] = e["name"]
        satellite["image"] = ""
        satellite["year_launched"] = e["year_launched"]
        satellite["type"] = e["typeName"]
        satellite["agency"] = e["agency"]
        satellite["host_pid"] = -1
        satellite["star_pid"] = -1
        satellite["galaxy_pid"] = -1
        satellites.append(satellite)

    return satellites
