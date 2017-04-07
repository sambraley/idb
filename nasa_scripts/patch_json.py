import json
import collections

satellite_file = "data/satellites.json"
patch_file = "satellite_patch.json"

def patch_json(target_file, fix_file, key):
    with open(target_file) as json_file, open(patch_file) as patch_json_file:
        patched_file = get_key_dict(json.load(json_file), key)
        
        patch = get_key_dict(json.load(patch_json_file), key)
        
        apply_patch(patched_file, patch)
        patched_file = strip_names(patched_file)
        
        outfile = open(target_file, 'w')
        json.dump(patched_file, outfile, indent="\t")
        outfile.close()

def get_key_dict(json_list, key):
    name_dict = collections.OrderedDict()
    for entry in json_list:
        name_dict[entry[key]] = entry
    
    return name_dict

def strip_names(name_dict):
    json_list = []
    for entry in name_dict:
        json_list.append(name_dict[entry])

    return json_list

def apply_patch(to_patch, patch):
    num_removed = 0
    keys = list(to_patch.keys())
    for i in range(0, len(keys)):
        entry = keys[i]
        if entry in patch:
            if "remove" in patch[entry]:
                to_patch.pop(entry)
                num_removed += 1
            else:
                for key in patch[entry]:
                    to_patch[entry][key] = patch[entry][key]
        if entry in patch and "remove" not in patch[entry] and 'pid' in to_patch[entry]:
            to_patch[entry]['pid'] -= num_removed

patch_json(satellite_file, patch_file, 'name')
