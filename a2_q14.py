# 14. Write a Python program to remove duplicates from a list

# we can use the property of set to get unique elemnets in our list
# as set only store unique elements
lst=[11,12,11,13,14,11,23,12,23]
def unique():
    print(list(set(lst))) #here the list gets converted into set with only unique elements and that set gets converted into the list

unique()
