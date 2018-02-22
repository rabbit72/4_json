import json
import sys


def load_data(path):
    with open(path) as f:
        obj_json = json.loads(f.read())
    return obj_json


def pretty_print_json(obj_json):
    print(json.dumps(obj_json, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    file_path = sys.argv[1]
    obj_json = load_data(file_path)
    pretty_print_json(obj_json)
