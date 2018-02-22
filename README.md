# Prettify JSON

This module is used to output the file to the console in a readable form.

# Quickstart

```bash
$ python pprint_json.py <path to file>
```
###Example of script launch on Linux, Python 3.5:
 Input data from file:
```json
{"firstName":"John","lastName":"Smith","address":{"streetAddress":"101, Victoria street","city":"London","postalCode": "SW1E"},"phoneNumbers":["+44 20 123 1234"]}
```

Output to console:
```json
{
    "address": {
        "city": "London",
        "postalCode": "SW1E",
        "streetAddress": "101, Victoria street"
    },
    "firstName": "John",
    "lastName": "Smith",
    "phoneNumbers": [
        "+44 20 123 1234"
    ]
}
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
