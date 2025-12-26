# Dictionaries are unordered collections of key-value pairs - mutable and indexed - use curly braces {}
# Keys must be unique and immutable (strings, numbers, or tuples) whereas values can be of any data type and can be duplicated
person = {"name": "Pavan", "age": 25, "city": "New York"}
print(person)
# Accessing values using keys
print(person["name"])  # Output: Pavan 
print(person["age"])   # Output: 25
# Adding a new key-value pair
person["profession"] = "Engineer"   
print(person)
# Modifying an existing value
person["age"] = 26  
print(person)
