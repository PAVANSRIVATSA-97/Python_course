# 1.1
fruits = ["apple", "banana", "cherry",]
print(fruits[0])
fruits[1] = "orange"
print(fruits)
print(len(fruits))

# 1.2
numbers = [1,2 ,3,4,5,6,7,8,9,10]
print(numbers[0:3])
print(numbers[7:10])

#2.1
numbers = [5,2,9,1,7]
numbers.sort()
print(numbers)
numbers.append(10)
print(numbers)
numbers.remove(2)
print(numbers)

#2.2
names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names)

# 3.1
cordinates = (10, 20)
print(cordinates)
list1 = list(cordinates)
print(list1)
list1[0] = 50
print(list1)
updated_cordinates = tuple(list1)
print(updated_cordinates)

# 4.1
my_set = {1,2,3,3,4}
print(my_set)
my_set.add(5)
my_set.remove(2)
print(my_set)

# 4.2
a = {1,2,3,4}
b = {3,4,5,6}
c = a.union(b)
print(c)    
d = a.intersection(b)
print(d)    
e = a.difference(b)
print(e)

#5.1
student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
student.update({"city": "Delhi"})
print(student)

#5.2
friends = {"Alice": 2512313, "Bob": 2213462, "Charlie": 2346752}
print(friends.keys())
print(friends.values())
print(friends.items())

# n = int(input("Enter range of number: "))
# list = []
# for i in range(n):
#     i = int(input("Enter number:"))
#     list.append(i)
# list.sort()
# print(list)
# set1 = set(list)
# print(set1)

# Dictionary of products and their prices
products = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 300,
    "Smartphone": 800
}

# Finding the product with the highest price
# We use max() on the dictionary keys, but tell it to compare their values
highest_price_product = max(products, key=products.get)

print(f"The most expensive product is: {highest_price_product}")
print(f"Price: ${products[highest_price_product]}")
    