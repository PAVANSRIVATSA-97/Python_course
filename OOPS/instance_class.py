class Student:
    school = "RPS" # class attribute
    def __init__(self, name, age, grade, school): # constructor method
        self.name = name  # instance attribute
        self.age = age    # instance attribute
        self.grade = grade # instance attribute
        self.school = school  # instance attribute
    def print_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}")
    
s1 = Student("Pavan", 21, "A", "DPS")
print(s1.school) # RPS will be overridden by instance attribute "DPS". if instance attribute is not present, class attribute will be accessed.
print(Student.school)  # accessing class attribute using class name
s1.print_info()
print(dir(s1))  # prints all attributes and methods of the instance s1
