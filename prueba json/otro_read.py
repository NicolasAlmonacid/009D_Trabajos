import json
with open("my_data.json", "r") as f:
    json_object = json.loads(f.read())
    f.read()
    print(json_object["people"][1]["name"])