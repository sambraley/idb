import json
import urllib.request
import sys

def scrape(w) :
    data = request_data()
    data = filter_data(data)
    data = transform_data(data)
    write_data(w, data)

def request_data() : 
    base = "http://simbad.u-strasbg.fr/simbad/sim-sam?"
    mode = "OutputMode=LIST"
    limit = "maxObject=1000"
    criteria = "Criteria=otype=%27G%27"
    output_format="output.format=ASCII"
    object_type = "list.otypesel=on"
    object_type_disp = "otypedisp=3"
    coor = "list.coo1=on"
    frame = "frame1=ICRS"
    coor_disp = "coodisp1=d2"
    redshift = "list.rvsel=on"
    redshift_disp = "rvDisplay=Z"
    morph_type = "list.mtsel=on"
    size = "list.sizesel=on"
    flux = "list.fluxsel=off"
    bib = "list.bibsel=off"
    notes = "list.notesel=off"

    attrs = [mode, limit, criteria, output_format, object_type, object_type_disp, \
             coor, frame, coor_disp, redshift, redshift_disp, morph_type, size, flux, bib, notes]

    request_str = base + implode(attrs, "&")
    raw = urllib.request.urlopen(request_str).read().decode("utf-8")
    return ascii_to_json(raw)
    

def implode(i, delimeter) :
    imploded = "";
    for e in i :
        imploded += e + delimeter

    imploded = imploded[:-len(delimeter)]
    return imploded


def ascii_to_json(ascii_data) :
    i = iter(ascii_data.splitlines())
    for _ in range(0, 7) :
        next(i)
    
    keys = [key.strip() for key in next(i).split("|")]
    next(i)

    data = []
    for line in i :
        if "|" in line :
            values = [value.replace("~", "").strip() for value in line.split("|")]
            datum = {t[0]:t[1] for t in zip(keys, values)}
            data.append(datum)
    return data
    
def transform_data(data) : 
    galaxies = []
    for datum in data :
        galaxy = {}
        galaxy["pid"] = -1
        galaxy["name"] = datum["identifier"]
        galaxy["image"] = ""
        galaxy["ra"] = float(datum["coord1 (ICRS,J2000/2000)"].split(" ")[0])
        galaxy["dec"] = float(datum["coord1 (ICRS,J2000/2000)"].split(" ")[0][1:])
        galaxy["type"] = datum["morph. type"]
        galaxy["redshift"] = datum["redshift"]
        galaxy["size"] = datum["ang. size"]
        galaxies.append(galaxy)
    return galaxies

def filter_data(data) : 
    required_attrs = ["identifier","coord1 (ICRS,J2000/2000)","redshift", "morph. type", "ang. size"]
    return list(filter(lambda d : has_attrs(d, required_attrs), data))

def has_attrs(d, attrs) :
    for attr in attrs :
        if attr not in d or d[attr] == "" :
            return False
    return True

def write_data(w, data) :
    json.dump(data, w, indent="\t")
