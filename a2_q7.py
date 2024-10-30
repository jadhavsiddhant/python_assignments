# 7. W AP to demonstrate how positional arguments and keyword arguments 
# can be used in functions

def display_student_info(name, age, grade="Not Assigned"):
    print(f"Student Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")

# Calling the function with both positional and keyword arguments
display_student_info("Alice", 14, grade="A")
display_student_info("Bob", 15)
display_student_info("Charlie", 13, grade="B")
