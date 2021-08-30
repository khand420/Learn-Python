import json

data = '{"var1":"khand", "var2":55}'
print(data)
parsed = json.loads(data)
print(parsed['var1'])

# TASK1 - json.load 

data2 = {
    "channel_name": "code2hell",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
jscomp = json.dumps(data2)
print(jscomp)



# TASK2 - json.dump 
print("hello world")