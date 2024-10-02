# Object-oriented programming (OOP) is a development paradigm 
# built on the concept of objects.
    # Real Life entity.
    # Data in Feilds
    # MMethods or behaviours of these objects

# Prasad
# ZhonKai
# Joseph

# Data abstraction 

# One of the most essential concepts of Python OOPs which is used 
# to hide irrelevant details from the user and show the details that are relevant to the users. 

# It enables programmers to hide complex implementation details while just showing users 
#the most crucial data and functions.

# In Python, we can achieve data abstraction by using abstract classes and abstract 
# classes can be created using abc (abstract base class) module and abstractmethod of abc module.

# # Code from PPT

# # Import required modules
# from abc import ABC, abstractmethod

# # Create Abstract base class
# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     @abstractmethod
#     def printDetails(self):
#         pass

#     def accelerate(self):
#         print("Speed up...")

# # Create a child class
# class Hatchback(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)

#     def Sunroof(self):
#         print("Not having this feature")

# # Create a child class
# class Suv(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)

#     def Sunroof(self):
#         print("Available")

# # Create an instance of Hatchback
# car1 = Hatchback("Maruti", "Alto", "2022")
# car1.printDetails()
# car1.accelerate()



# My Abstract Code _

from abc import ABC, abstractmethod

# Abstract class defining a Shape
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Concrete class Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Concrete class Square inheriting from Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

# Function to print area of any Shape
def print_area(shape):
    print(f"Area: {shape.calculate_area()}")

# Creating instances and demonstrating abstraction
circle = Circle(5)
square = Square(4)

print_area(circle)  # Prints the area of the circle
print_area(square)  # Prints the area of the square



# Components of OOP:
        # Objects & Classes
        # Inheritence
        # Polymorphism
        # Encapsulation
        # Abstraction