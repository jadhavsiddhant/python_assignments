# Write a Python program to create a calculator class. Include methods for
# basic arithmetic operations.

class Calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def addition(self):
        return self.n1 + self.n2
    
    def subtraction(self):
        return self.n1-self.n2
    
    def multiplication(self):
        return self.n1 * self.n2
    
    def division(self):
        return self.n1/self.n2
    
x = Calculator(10, 15)

print('multiplication:',x.multiplication())
print('addition',x.addition())
print('subtraction', x.subtraction())
print('division',x.division())


