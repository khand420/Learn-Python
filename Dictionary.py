# Dictionary is a key value pairs

# {} -> dictionary in python 
dictionary = {}
print(type(dictionary))

# () -> touple in python 
# [] -> List in python 


d ={"khand": "Burger", "Raza": "Choclate", "Muskan": "Roti", "Keshav": "Daru", "Rohit":{"M":"maggie", "L":"Rice", "D":"Fish"}}


# ADD 
d ["Maryam"] = "Junk-Food"
d [420] = "kabab"
print(d)

# Delete
del d[420]
print(d)

# Copy
# d1 = d.copy()
# del d1["khand"]
# print(d1)

# GET
print(d.get("khand"))


# Update
d.update({"keshaw": "pepsi"})
print(d)

print( d.keys())
print(d.items())





