# 9. WAP to demonstrate how variable length arguments are used in functions.

# in here *args allows us to accept as many argument as possible 

def calculate_sum(*args):
    x=sum(args)
    print(x)

calculate_sum(10,20,30,40,50)