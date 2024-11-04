# 2. Write a Python class named Circle. Declare an instance variable, radius and 
#  two methods that will compute the area and the perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return math.pi * (self.radius ** 2)  
    def perimeter(self):
        return 2 * math.pi * self.radius  


circle1 = Circle(5)
print("Area:", circle1.area())         
print("Perimeter:", circle1.perimeter())  
    
