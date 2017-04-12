import webbrowser
import os
import json
import sys

objects_file = open(sys.argv[1], "r+");
objects = json.load(objects_file)

base_html = open("img_scraper_html_base.txt", "r");
base_html_str = base_html.read();
base_html.close()
base_html_str = base_html_str.replace("spacecowboy_ra", str(objects[int(sys.argv[2])]["ra"]))
base_html_str = base_html_str.replace("spacecowboy_dec", str(objects[int(sys.argv[2])]["dec"]))
base_html_str = base_html_str.replace("spacecowboy_file", "object_" + str(int(sys.argv[2])) + "_img.json")

html_file = open("img_scraper.html", "w")
html_file.write(base_html_str)
html_file.close()

url = "file:///Z:/Documents/College/2017_01%20(Spring)/CS373/idb/nasa_scripts/img_scraper.html"
webbrowser.open_new(url)
