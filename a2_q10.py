# 10. WAP to demonstrate how variable length keyword arguments 
# are used in functions.

# in here **kwargs handle varibale length keyword , here this arguments are 
# passed as a dictonary where parameter are keys and values are assigned to those keys

def display_person_info(**kwargs): #keyword arguments kwargs
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
    print("\n")  # For better readability

display_person_info(name="Alice", age=25, city="New York", occupation="Engineer")
display_person_info(name="Bob", age=30, city="San Francisco")
display_person_info(name="Charlie", age=22, hobby="Photography", favorite_color="Blue")
