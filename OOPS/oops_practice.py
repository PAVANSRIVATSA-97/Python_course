#1.1
class car:
    def drive(self):
        print("The car is moving")

c = car()
c.drive()

#2
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")

p1 = person("Pavan", 24)
p1.print_info()

#3
class Animal:
    location = "Forest"
    def sound(self):
        print("Some sound")
    
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

d = Dog()
print(d.location)
d.sound()