# there are not many built-in methods for tuples as they are immutable
# count() - returns the number of occurrences of a specified value
names = ("Pavan", "Srilu", "Anu", "Kalyan", "Pavan", "Pavan")
print(names)
count_pavan = names.count("Pavan")  # counts how many times "Pavan" appears in the tuple
print(f"'Pavan' appears {count_pavan} times in the tuple.")
# index() - returns the index of the first occurrence of a specified value
index_anu = names.index("Anu")  # finds the index of "Anu" in the tuple
print(f"'Anu' is located at index {index_anu} in the tuple.")