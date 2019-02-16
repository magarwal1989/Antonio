import json

# return the data object from the json file
def parse_json_from_file(filename):
    with open(filename) as f:
        data = json.load(f)
    return data
