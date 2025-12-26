s = {1, 2, 3, 4, 5, 5, 4}  # duplicate values will be ignored
v = {2,4,6}

a = s.union(v)  # union of two sets - combines all unique elements from both sets
print("Union:", a)
b = s.intersection(v)  # intersection of two sets - elements common to both sets
print("Intersection:", b)
c = s.difference(v)  # difference of two sets - elements in s but not in v
print("Difference (s - v):", c)