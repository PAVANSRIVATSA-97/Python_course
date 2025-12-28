'''class employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def __add__(self, other): # dunder method to add two employee salaries
        return self.age + other.age

    def __repr__(self): # dunder method to represent the object as a string
        return f"Employee(Name: {self.name}, Salary: {self.salary}, Age: {self.age})"
    
    def __str__(self): # dunder method to return a string representation of the object
        return f"{self.name} earns {self.salary} and is {self.age} years old."
    
    def __len__(self): # dunder method to return the length of the employee name
        return len(self.name)
        
e1 = employee("Pavan", 50000, 24)
e2 = employee("Srilu", 60000, 22)   
print(e1 + e2)  # adds the salaries of both employees using __add__ dunder method
print(repr(e1))  # prints the employee details using __repr__ dunder method
print(str(e2))  # prints the string representation of the employee using __str__ dunder method
print(len(e1))  # prints the length of the employee name using __len__ dunder method '''

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # dunder method to add two vectors
        return vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other): # dunder method to subtract two vectors
        return vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other): # dunder method to multiply two vectors
        return vector(self.x * other.x, self.y * other.y)
    
    def __str__(self): # dunder method to divide two vectors
        return f"Vector({self.x}, {self.y})"
    
v1 = vector(2, 3)
v2 = vector(4, 5)
v3 = v1 + v2
print(v3)  # prints the result of vector addition
v4 = v3 - v1
print(v4)  # prints the result of vector subtraction
v5 = v1 * v2
print(v5)  # prints the result of vector multiplication

