import glob
import json
from os import path
from shutil import move
from collections import OrderedDict


cercle_icons = "./icons/circle/48/"
square_icons = "./icons/square/48/"
data_file = "./data.json"

# The icons map dict should follow this format
# Old icon name as a key
# The new icon name as a value
icons_map = {
    "steam_icon_250420": "8bitmmo"
}

# Read the database file
with open(data_file, 'r') as db_obj:
    data = json.load(db_obj, object_pairs_hook=OrderedDict)


def _move(old_name, new_name, directory):
    old_name = path.join(path.realpath(directory), old_name) + ".svg"
    new_name = path.join(path.realpath(directory), new_name) + ".svg"

    if path.exists(old_name):
        move(old_name, new_name)


to_delete = []
for old_name, new_name in icons_map.items():
    _move(old_name, new_name, cercle_icons)
    _move(old_name, new_name, square_icons)
    if data.get(old_name):
        data[new_name] = data[old_name]
        to_delete.append(old_name)

for entry in to_delete:
    del data[entry]

with open(data_file, 'w') as db_obj:
    json.dump(data, db_obj, indent=4)
