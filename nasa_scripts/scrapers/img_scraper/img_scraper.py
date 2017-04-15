import webbrowser
import os
import json
import sys
import time

objects_file = open(sys.argv[1], "r+");
objects = json.load(objects_file)

loop = True
index = 0
if len(sys.argv) == 3:
    index = int(sys.argv[2])
    loop = False
    
while True:
    base_html = open("img_scraper_html_base.txt", "r");
    base_html_str = base_html.read();
    base_html.close()
    base_html_str = base_html_str.replace("spacecowboy_ra", str(objects[index]["ra"]))
    base_html_str = base_html_str.replace("spacecowboy_dec", str(objects[index]["dec"]))
    base_html_str = base_html_str.replace("spacecowboy_file", "object_" + str(index) + "_img.json")

    html_file = open("img_scraper.html", "w")
    html_file.write(base_html_str)
    html_file.close()

    url = "file:///Z:/Documents/College/2017_01%20(Spring)/CS373/idb/nasa_scripts/scrapers/img_scraper/img_scraper.html"
    webbrowser.open_new(url)
    
    index += 1
    time.sleep(5)
    
    if index % 40 == 0:
        time.sleep(15)
    
    if not loop or index == len(objects):
        break