import json

compiled = open("compiled_planet_imgs.json", "w")
compiled_json = []

for i in range(0, 299):
		img_file = open("object_" + str(i) + "_img.json")
		img_json = json.load(img_file)
		img_dict = {"pid":i, "url":str(img_json["url"])}
		compiled_json.append(img_dict)

#print(compiled_json)
json.dump(compiled_json, compiled)
compiled.close()