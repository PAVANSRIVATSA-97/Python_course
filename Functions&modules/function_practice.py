# 1.1
def greet():
    print("Hello, welcome to the Python course!")
greet()
# 1.2
def square(num):
    return num * num
print(square(6))
# 1.3
def full_name(first_name, last_name):
    return first_name + " " + last_name
print(full_name("John", "Doe"))
# 1.4
def calculate_area(length, width=10):
    return length * width
print(calculate_area(5,3))
print(calculate_area(7))
# 1.5
fun= lambda x, y: x + y
print(fun(4, 5))