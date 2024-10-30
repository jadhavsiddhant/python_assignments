# 6. W AP to demonstrate the functionality of keyword argument in functions

# Using keyword arguments makes it clear what each argument represents,
#  improving readability, and you can change the argument order without 
# affecting the function call’s result.

def si(amount,time,roi):

    x=amount*time*roi
    xi=x/100
    print("simple intrest on the given amount",xi)

si(roi=10000,time=3,amount=8)