import json
import sys


def load_data(path):
    with open(path) as file_json:
        deserialized_json = json.loads(file_json.read())
        return deserialized_json


def pretty_print_json(deserialized_json):
    print(json.dumps(deserialized_json, sort_keys=True,
                     indent=4, ensure_ascii=False))


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        deserialized_json = load_data(file_path)
        pretty_print_json(deserialized_json)
    except IndexError:
        sys.exit('No path to file. Try again entering the path')
    except FileNotFoundError:
        sys.exit('File on the entered path was not found.'
                 'Check path to file')
    except json.decoder.JSONDecodeError:
        sys.exit('File on the entered path not JSON format')
