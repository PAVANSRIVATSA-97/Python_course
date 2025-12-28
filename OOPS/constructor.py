# Constructor in Python OOPS
# A constructor is a special method in a class that is automatically called when an object of the class is created.
# It is used to initialize the attributes of the object.
class vote:
    def __init__(self, name, age, city): # constructor method - called when an object of the class is created
        self.peru = name # attribute of the class
        self.vayasu = age # attribute of the class
        self.ooru = city
    def display_info(self):
        print(f"Name: {self.peru}\nAge: {self.vayasu}\nCity: {self.ooru}\n")

v1 = vote("Srilu", 20, "Bangalore")
v1.display_info()
v2 = vote("Anu", 22, "Chennai")
v2.display_info()
