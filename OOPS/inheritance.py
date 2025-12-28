class car:
    year = 2020
    def __init__(self, name, model):
        self.name = name
        self.model = model
    def display(self):
        print("This is a", self.name, "of model", self.model, "manufactured in", self.year)

class electric_car(car):  # inheritance - electric_car is derived class, car is base class
    def __init__(self, name, model, battery_capacity):
        super().__init__(name, model)  # calling the constructor of the base class
        self.battery_capacity = battery_capacity
    def display_battery_info(self):
        print(f"{self.name} has a battery capacity of {self.battery_capacity} kWh")

ecar1 = electric_car("Tesla", "Model S", 100)
ecar1.display()  # method from base class
ecar1.display_battery_info()  # method from derived class

