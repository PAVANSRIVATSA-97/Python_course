class friends:
    location = "Hyderabad"  # class variable - shared by all instances of the class
    def __init__(self, name, age,): # it is a constructor method used to initialize the attributes of the object
        self.name = name
        self.age = age 
          # instance variable - unique to each instance of the class
    @classmethod
    def change_location(cls, new_location):
        cls.location = new_location  # changing class variable using class name

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nlocation: {self.location}\n")
# Every default method in a class will have 'self' as its first parameter which refers to the current instance of the class unless specified otherwise.
# Other methods can be created inside the class to perform various operations like static methods, class methods, instance methods etc.

    @staticmethod
    def sum(a, b): #-- if it is not a static method it will have self as first parameter 
        return a + b
    
f1 = friends("Pavan", 21)
f2 = friends("Anu", 22)
f1.display()
f2.display()
print(f2.sum(5, 10))  # calling static method using class name
print(friends.location)  # accessing class variable using class name
friends.change_location("Chennai")  # changing class variable using class method
print(friends.location)  # accessing updated class variable using class name
f1.display()
f2.display()