import json



with open('firstlast.json') as f:
    data = json.load(f)

#loop though JSON, strip data    
for x in data["Information"]:
    first = x["First_Name"]
    last = x["Second_Name"]
    print(last + ", " + first)