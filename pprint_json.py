import json
import sys


def load_data(path):
    try:
        with open(path) as file_json:
            try:
                deserialized_json = json.loads(file_json.read())
            except json.decoder.JSONDecodeError:
                print('File on the entered path not JSON format')
                sys.exit()
    except FileNotFoundError:
        print('File on entered path was not found. Check path to file.')
        sys.exit()
    return deserialized_json


def pretty_print_json(deserialized_json):
    print(json.dumps(deserialized_json, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
    except IndexError:
        print('No path to file. Try again entering the path.')
        sys.exit()
    deserialized_json = load_data(file_path)
    pretty_print_json(deserialized_json)
