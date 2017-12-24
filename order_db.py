import json
from collections import OrderedDict
from os import path

data_file = path.realpath("./data.json")


with open(data_file, 'r') as db_obj:
    data = json.load(db_obj, object_pairs_hook=OrderedDict)


for key, value in data.items():
    if value.get("linux"):
        symlinks = value["linux"].get("symlinks")
        if symlinks:
            data[key]["linux"]["symlinks"] = sorted(
                data[key]["linux"]["symlinks"], key=lambda name: name.lower())
    if value.get("android"):
        data[key]["android"] = sorted(
            data[key]["android"], key=lambda name: name.lower())

data = OrderedDict(sorted(data.items(), key=lambda entry: entry[0].lower()))

with open(data_file, 'w') as db_obj:
    json.dump(data, db_obj, indent=4)
