import json
import urllib.request
import sys
from Spacecowboy import implode
from urllib.parse import urlencode

url_fields = ["action=query","format=json"]
url_base = "https://en.wikipedia.org/w/api.php?"



def satellite_image_scrape():
	#read in from satellite json file
	satellites = json.loads(open('satellites.json').read())
	
	satellite_img_urls = dict()
	for satellite in satellites:
		name = satellite["name"]
		satellite_img_urls[name] = [] 
		search_fields = {'action': 'query', 'format': 'json', 'list':'search', 'srsearch':name}

		url_str = url_base + urllib.parse.urlencode(search_fields)
		
		raw = urllib.request.urlopen(url_str).read().decode("utf-8")

		wiki_title = json.loads(raw)["query"]["search"][0]["title"]

		img_search_fields = {'action': 'query', 'format': 'json', 'prop':'images', 'titles':wiki_title}

		url_str = url_base + urllib.parse.urlencode(img_search_fields)

		raw = urllib.request.urlopen(url_str).read().decode("utf-8")

		pages = json.loads(raw)["query"]["pages"]

		for page in pages.values():
			if "images" in page:
				#not all satellites have images
				for img in page["images"]:
					img_title = img["title"]
					img_info_fields = {'action': 'query', 'format': 'json', 'titles':img_title, 'prop':'imageinfo', 'iiprop': 'url'}
					url_str = url_base + urllib.parse.urlencode(img_info_fields)
					raw = urllib.request.urlopen(url_str).read().decode("utf-8")
					
					url = next(iter(json.loads(raw)["query"]["pages"].values()))["imageinfo"][0]["url"]

					satellite_img_urls[name].append({"title" : img_title, "url": url})


	satellite_img_urls_file = open ("satellite_img_urls.json", "w")
	json.dump(satellite_img_urls, satellite_img_urls_file, indent="\t")


satellite_image_scrape()
