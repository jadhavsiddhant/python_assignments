# 1. Create a person class with: 
# i) two instance variable: name, age.  
# ii) Create a parameterized constructor 

# a class is a blueprint for creating the object , it defines set of attributes 
# function that creates the objects

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = Person("Alice", 30)
print("Name:", p1.name)
print("Age:", p1.age)