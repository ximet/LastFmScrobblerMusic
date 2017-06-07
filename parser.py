import json

def parse_json(filename):
    with open(filename) as data_file:
        return json.load(data_file)
