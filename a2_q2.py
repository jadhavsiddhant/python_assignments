# 2. Write a Python function that takes a list and returns a new list with distinct elements from
# the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list():
    lst=[]
    n=int(input("number of integers you want to input in this list:"))
    for i in range(n):
        x=int(input("enter that integer:"))
        lst.append(x)

    print(list(set(lst)))
    
unique_list()

