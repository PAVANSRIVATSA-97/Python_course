# Class - A blueprint/template for creating objects. It defines a set of attributes and methods that the created objects will have.
# Object - An instance of a class. It is created using the class blueprint and can have its own unique attributes and behaviors.
# Pillar of OOPS:
# 1. Encapsulation - The bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data. Access to the data is typically provided through public methods.
# 2. Inheritance - A mechanism where a new class (derived class or child class) can inherit attributes and methods from an existing class (base class or parent class). This promotes code reusability and establishes a hierarchical relationship between classes.
# 3. Polymorphism - The ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name.
# 4. Abstraction - The concept of hiding the complex implementation details and showing only the essential features of the object. It helps in reducing complexity and increases efficiency by allowing the user to interact with the object at a higher level without needing to understand the intricate workings behind it.
# Example of a simple class and object in Python
# A class named 'Car' is defined with attributes like 'make', 'model', and 'year', and a method 'display_info' to display the car's information. --- this is the blueprint/template
# An object is that created using the Car template. ex- toyota,audi etc.