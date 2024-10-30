# 8. W AP to demonstrate the functionality of default argument in functions

def greet_user(name, greeting="Hello"): #hello is default argument 
    print(f"{greeting}, {name}!")

greet_user("Alice")
greet_user("Bob", "Good morning")
greet_user("Charlie", "Welcome")