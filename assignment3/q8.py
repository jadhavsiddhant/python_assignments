# 8. WAP to find the number of words in the given text file
# Hints:
# Use the split() method to separate words.

file = open("word.txt", "r")
content = file.read()
x=content.split()
words= len(x)

print("total no of words in the file is ", words)

