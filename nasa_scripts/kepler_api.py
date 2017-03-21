import urllib.request
import json

# kepler data at exoplanet archive requires no api key.
# only confirmed planets, the exoplanet table, should be used.
# There are only 3000+ confirmed planets
base_url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?"
exoplanet_table = "table=exoplanets"
attr = "select=pl_name,pl_radj,pl_bmassj,pl_orbper,pl_eqt"
req_format = "format=json"

request_str = base_url + exoplanet_table + "&" + attr + "&" + req_format

data = urllib.request.urlopen(request_str).read().decode("utf-8")
obj = json.loads(data)

planets = []

# filters out any results where an attribute was null
for d in obj :
    all_attr = True
    for key in d :
        if d[key] == None :
            all_attr = False
    
    if all_attr :
        planets += [d]

# Calculate derived attributes


print(len(planets))
print(planets[0])
