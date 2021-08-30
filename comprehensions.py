
# FOR LIST 

# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)
 
#  OR

# ls = [i for i in range(100) if i%3 == 0]

# print(ls)

# FOR DICTIONARY

# dict1 = {i: f"Item{i}" for i in range(1, 10001) if i%100==0}
dict1 = {i: f"Item{i}" for i in range(5)}
#  REVERSE DICTIONARY
dict2 = {value:key for key, value in dict1.items()}
print(dict1, "\n", dict2)
