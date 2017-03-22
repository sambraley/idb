import urllib.request
import json

def has_req_attr(d, req_attr) :
    for attr in req_attr :
        if attr in d and d[attr] is None:
            return False

    return True

# kepler data at exoplanet archive requires no api key.
# only confirmed planets, the exoplanet table, should be used.
# There are only 3000+ confirmed planets
base_url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?"
table = "exoplanets"
out_format = "json"

# Planet Attributes of Output:
#   pl_name - name of planet. usually the hostname and planet letter
#   pl_radj - radius of planet in Jupiter radii
#   pl_massj - mass of planet in Jupiter mass
#   pl_orbper - planet's orbital period in (Earth) days
#   pl_eqt - the planet equilibrium temperature (a calculate surface temperature)
planet_attrs = ["pl_name", "pl_radj", "pl_massj", "pl_orbper", "pl_eqt"]

# Stellar Attributes of output:
#   pl_hostname - stellar name most commonly used in literature
#   st_rad - stellar radius in solar radii
#   ra - right ascension in decimal degrees
#   dec - declination in decimal degrees
#   st_teff - effective temperature
#   st_mass - stellar mass in solar mass
stellar_attrs = ["pl_hostname", "st_rad", "ra", "dec", "st_teff", "st_mass"]

# Build Request String
request_str = base_url + "table=" + table + "&select="
for attr in planet_attrs :
    request_str += attr + ","
for attr in stellar_attrs :
    request_str += attr + ","
request_str = request_str[:-1]
request_str += "&format=" + out_format
print(request_str)

# Request data and filter it
raw_data = urllib.request.urlopen(request_str).read().decode("utf-8")
json_data = json.loads(raw_data)
json_data = list(filter(lambda d : has_req_attr(d, planet_attrs), json_data))
json_data = list(filter(lambda d : has_req_attr(d, stellar_attrs[1:]), json_data))

print(len(json_data))

# Results in 300 entries with all requred attributes

# Create list of planets

# Planet Attributes for IDB Model
#   name = pl_name
#   diamter = 2 * pl_radj * radius of jupiter
#   ra = ra
#   dec = dec
#   gravity = (Gravity Constant * pl_massj * mass of jupiter) / (pl_radj * radius of jupter ) ^ 2
#   orbital_period = pl_orbper
#   mass = pl_massj * mass of jupiter
#   temperature = pl_eqt
#   host = pl_hostname

radj = 69911 # radius of jupiter in kilometers
G = 6.67408 * (10 ** -20) # Gravitation constont km^3 kg^-1 s^-2
massj = 1.898 * (10 ** 27) # mass of jupiter in kg

planets = []

for d in json_data :
    planet = {}
    planet["name"] = d["pl_name"]
    planet["diamter"] = 2 * d["pl_radj"] * radj
    planet["ra"] = d["ra"]
    planet["dec"] = d["dec"]
    planet["gravity"] = (G * d["pl_massj"] * massj) / (( d["pl_radj"] * radj) ** 2)
    planet["orbital_period"] = d["pl_orbper"]
    planet["mass"] = d["pl_massj"] * massj
    planet["temperature"] = d["pl_eqt"]
    planet["host"] = d["pl_hostname"]

    planet["picture"] = None

    planets.append(planet)

print(len(planets))

# Create list of stars

# Star Attributes for IDB Model
#   name = pl_hostname or hd_name
#   diameter = st_rad
#   ra = ra
#   dec = dec
#   temperature = st_teff
#   mass = st_mass

stars = []

for d in json_data :
    star = {}
    star["name"] = d["pl_hostname"]
    star["ra"] = d["ra"]
    star["dec"] = d["dec"]
    star["temperature"] = d["st_teff"]
    star["mass"] = d["st_mass"]
    star["picture"] = None
    star["distance"] = None
    stars.append(star)

print(len(stars))

# Create three instances of each model

planets_file = open('planets_data.json', 'w')
json.dump(planets[:3], planets_file, indent="\t")
planets_file.close()

stars_file = open('stars_data.json', 'w')
json.dump(stars[:3], stars_file, indent="\t")
stars_file.close()
