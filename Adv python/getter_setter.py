# class dog:
#     def __init__(self, name, breed):
#         self.name = name          
#         self.breed = breed 

#     @property
#     def name(self):
#         return self.peru

#     @name.setter
#     def name(self, value):
#         self.peru = value

#     def print_info(self):
#         print(f"Name: {self.name}\nBreed: {self.breed}")

# d1 = dog("Tommy", "Labrador")
# print(d1.name)
# d1.name = "Rocky"
# d1.print_info()

class student:
    def __init__(self, name, age, school_name):
        self.name = name
        self.age = age
        self._school_name = school_name  # private attribute

    @property
    def school(self):
        return self._school_name 
    
    @school.setter
    def school(self, value):
        self._school_name = value
    
    def print_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSchool: {self.school}")

s1 = student("Pavan", 21, "RPS")
print(s1.school)    
s1.school = "DPS"
s1.print_info()

