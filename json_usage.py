import json


if __name__ == '__main__':
    json_string = """{
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }
    """

    data = json.loads(json_string)

    print data['president']
    print data['president']['name']

