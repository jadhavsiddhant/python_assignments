# 1. Write a Python function that accepts a string and counts the number of upper and lower
# case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def up_lowcount():
    countu=0
    countl=0
    x=input("enter any string: ")
    for i in x:
        if i.isupper():
            countu+=1
           
        elif i.islower():
            countl+=1
            
    print("no of lowercase cahrecter",countl)
    print("no of upper case charecter:",countu)

up_lowcount()
        

