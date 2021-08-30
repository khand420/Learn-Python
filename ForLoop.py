list1 = [["khand", 1], ["raza", 2], ["amit", 4], ["siva", 6]]

dict1 = dict(list1)

for item in dict1:
    print(item)

# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)   



items = [int, float, "khand", 3, 4, 54, 43, 53, 56,7,3,3,344,432,22,12]
for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)

