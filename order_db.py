import json
from collections import OrderedDict
from os import path

data_file = path.realpath("./data.json")

# Read the database file
with open(data_file, 'r') as db_obj:
    data = json.load(db_obj, object_pairs_hook=OrderedDict)


def sort(liste, key_=None):
    """Sort a list, insensitive case."""
    if key_:
        return sorted(liste, key=lambda entry: entry[key_].lower())
    return sorted(liste, key=lambda entry: entry.lower())


for key, value in data.items():
    if value.get("linux"):
        symlinks = value["linux"].get("symlinks")
        if symlinks:
            # Sort symlinks
            symlinks = sort(symlinks)
            data[key]["linux"]["symlinks"] = symlinks
    # Sort android icons
    if value.get("android"):
        data[key]["android"] = sort(data[key]["android"])

# Sort icons key's
data = OrderedDict(sort(data.items(), 0))

with open(data_file, 'w') as db_obj:
    json.dump(data, db_obj, indent=4)
