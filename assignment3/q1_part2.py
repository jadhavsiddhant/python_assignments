# 2. Create a student class. Inherit person class in Student class.  
# Student class have: 
# i) instance variable: rollno and stream.  
# ii) Create a parameterized constructor to initialize all instance variables of  student class as 
# well as Person class 
# iii)Instance method: display() to print name, age, rollno and stream Create an 
# object of Student class and call display method 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,stream,rollno):
        super().__init__(name,age)
        self.stream=stream
        self.rollno=rollno

    def display(self):
        print(f"Name:{self.name},Age:{self.age},Stream:{self.stream},Rollno:{self.rollno}")

s1=Student('siddhant',18,'CS',100)
s1.display()
