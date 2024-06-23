import json
myDict = {
        "people" :[
            {
                "name": "Ben",
                "age": 23,
                "height": 5.6,
            },
             {
                "name": "Bob",
                "age": 25,
                "height": 5.9,
            },
             {
                "name": "Ben",
                "age": 29,
                "height": 5.8,
            },
        ]
} 

json_string = json.dumps(myDict, indent=4)

with open("my_data.json", "w") as f:
    f.write(json_string)