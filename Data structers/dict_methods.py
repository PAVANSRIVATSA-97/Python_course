dict = {"name": "Pavan", "age": 21, "city": "Hyderabad"}
print(dict.keys())  # prints all the keys in the dictionary
print(dict.values())  # prints all the values in the dictionary 
print(dict.items())  # prints all key-value pairs as tuples in a list
dict.update({"age": 22})  # updates the value for the specified key 
print(dict)
dict.update({"profession": "Developer"})  # adds a new key-value pair to the dictionary
print(dict)
dict.pop("city")  # removes the key-value pair with the specified key
print(dict)
dict.clear()  # removes all key-value pairs from the dictionary
print(dict)
# Example of dictionary comprehension
squares = {x: x*x for x in range(1, 6)}  # creates a dictionary of squares of numbers from 1 to 5
print(squares)