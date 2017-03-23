import json
import urllib.request

def implode_query(query_attrs) :
	query = []
	for key in query_attrs :
		query.append(key + "=" + query_attrs[key])
	return "&".join(query)

base_url = "https://simbad.u-strasbg.fr/simbad/sim-sam?"
query_attrs = {}
query_attrs["coodisp"] = "d"
query_attrs["list.rvsel"] = "on"
query_attrs["rvDisplay"] = "Z"
query_attrs["list.spsel"] = "off"
query_attrs["list.notesel"] = "off"
query_attrs["list.bibsel"] = "off"
query_attrs["list.fluxsel"] = "off"
query_attrs["list.sizesel"] = "on"
query_attrs["list.mtsel"] = "on"
query_attrs["output.format"] = "ascii"
query_attrs["Criteria"] = "otype=%27G%27"
query_attrs["OutputMode"] = "LIST"
query_attrs["maxObject"] = "3"


query_str = base_url + implode_query(query_attrs)

raw_data = urllib.request.urlopen(query_str).read().decode("utf-8")

# transform into json

