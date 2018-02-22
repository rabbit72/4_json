import json
import sys


def load_data(path):
    with open(path) as f:
        data = json.loads(f.read())
    return data


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    filepath = sys.argv[1]
    data = load_data(filepath)
    pretty_print_json(data)
