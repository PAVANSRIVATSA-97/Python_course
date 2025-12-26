# Tuples are immutable lists - ordered collection of items of any data type - cannot be changed(modified) unlike lists which are mutable
# Tuples use parentheses () whereas lists use square brackets []
# we use tuples when we want our collecton not to be changed accidentally like location coordinates, RGB values, etc.
names = ("Pavan", "Srilu", "Anu", "Kalyan")
print(names)
print(names[2])
# names[1] = "Alpha"  # This will raise an error because tuples are immutable same as strings
# print(names)
# string = "Hello World"
# print(string[4])
# string[4] = 'a'  # This will also raise an error because strings are immutable

list = [1]
print(list)
tuple1 = (1)
print(tuple1)  # this is not a tuple, this is an integer within parentheses
tuple = (1, )  # single element tuple should have a comma after the element
print(tuple)

tuple2 = (1, 2, 3, 4, 5) # we can assign the elements of a tuple to multiple variables
a, b, c, d, e = tuple2  # unpacking a tuple into multiple variables
print(a, b, c, d, e)