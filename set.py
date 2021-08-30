
# l = [1, 4, 5, 75, 3]

# set_from_list = set(l)
# print(set_from_list)


s = set()

s.add(1)
s.add(3)
s.add(4)
# s.remove(3)

# UNION 
# s1 = s.union({1,2,4})
# print(s1)

# INTERSECTION 
# s2 = s.intersection({1,2,5,})
# print(s, s2)
# print(max(s))

# DISJOIN (T/F)
s3= {5,6,7}
print(s.isdisjoint(s3))