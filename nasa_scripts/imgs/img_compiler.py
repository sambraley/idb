import json
import os
import sys

source = sys.argv[1]
destination = sys.argv[2]

compiled = open(destination, "w")
compiled_json = []

for file in os.listdir(source):
		img_file = open(os.path.join(source, file))
		img_json = json.load(img_file)
		compiled_json += [img_json]

json.dump(compiled_json, compiled)
compiled.close()