s = {"pavan", 3.5, "srilu", 42, "anu"}
print(s)
s.add("kalyan")  # adding an element to the set
print(s)
s.remove(3.5)  # removing an element from the set 
print(s)
s.add("anu")  # trying to add a duplicate element, will have no effect
print(s)
s.discard("not_in_set")  # trying to discard an element not in the set, will have no effect
print(s)
s.remove("not_in_set")  # trying to remove an element not in the set, will raise a KeyError
print(s)    
s.clear()  # removes all elements from the set
print(s)
