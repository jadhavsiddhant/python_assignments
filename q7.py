# 7. Create a class hierarchy for different types of geometric shapes, including  circles, rectangles, and triangles, using inheritance. 
# Tasks: 
# A. Define a base class called Shape with common attributes  
# like colour and area. 
# B. Implement subclasses for specific shape types such  
# as Circle, Rectangle, and Triangle. Each subclass should inherit  from the Shape class. 
# C. Incorporate additional attributes and methods specific to each  shape type. For example, a Circle class might have attributes  
# like radius and methods like calculate_area. 
# D. Use inheritance to create subclasses representing variations within  each shape type. For example, within the
# Rectangle class, create  subclasses for Square and Parallelogram. 
# E. Implement methods or attributes in the subclasses to demonstrate  how inheritance 
# allows for the sharing of attributes and methods  from parent classes. 
# F. Create instances of the various shape classes and test their  functionality to ensure that 
# attributes and methods work as  expected
import math

# Base class
class Shape:
    def __init__(self, colour):
        self.colour = colour

    def area(self):
        raise NotImplementedError("Subclasses should implement this!")

# Circle subclass
class Circle(Shape):
    def __init__(self, radius, colour):
        super().__init__(colour)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height, colour):
        super().__init__(colour)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Square subclass inheriting from Rectangle
class Square(Rectangle):
    def __init__(self, side_length, colour):
        super().__init__(side_length, side_length, colour)

# Parallelogram subclass inheriting from Rectangle
class Parallelogram(Rectangle):
    def __init__(self, base, height, colour):
        super().__init__(base, height, colour)

# Triangle subclass
class Triangle(Shape):
    def __init__(self, base, height, colour):
        super().__init__(colour)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Testing the functionality
if __name__ == "__main__":
    # Creating instances of different shapes
    circle = Circle(5, "Red")
    rectangle = Rectangle(4, 6, "Blue")
    square = Square(3, "Green")
    parallelogram = Parallelogram(5, 4, "Yellow")
    triangle = Triangle(6, 3, "Purple")

    # Calculating and printing the areas
    print(f"Circle Area: {circle.calculate_area():.2f}, Colour: {circle.colour}")
    print(f"Rectangle Area: {rectangle.calculate_area()}, Colour: {rectangle.colour}")
    print(f"Square Area: {square.calculate_area()}, Colour: {square.colour}")
    print(f"Parallelogram Area: {parallelogram.calculate_area()}, Colour: {parallelogram.colour}")
    print(f"Triangle Area: {triangle.calculate_area()}, Colour: {triangle.colour}")