##json.loads
import json

file_name = "simple.json"

with open(file_name, "r") as f:
    data = json.load(f)

print(type(data.get("friends")))



##json.dumps
import json
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Chris", 30)

with open("p1.json", "w") as f:
    json.dump(p1.__dict__, f, indent=4)

##Work with REST APIS
# First, pip install requests
import requests
import json
import pprint as pp

req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

data = json.loads(req.text)
pp.pprint(data, indent=8)

##json.dumps example

str_json = json.dumps(data)

print(str_json)
print(type(str_json))