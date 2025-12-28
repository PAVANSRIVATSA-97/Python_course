# creating a class 'voter' that has details like name, age, city etc
class Voter:
    name1 = ""
    age = 0
    city = ""
    def display_details(self): # self refers to the current instance of the class and it is mandatory to include it as the first parameter in instance methods
        print(f"Name: {self.name1}\nAge: {self.age}\nCity: {self.city}\n")
# creating an object 'voter1' of class Voter - specified instance of the class
voter1 = Voter()
voter1.name1 = "Pavan"   # 
voter1.age = 21
voter1.city = "Hyderabad"
voter1.display_details()  # calling the method to display voter1 details



