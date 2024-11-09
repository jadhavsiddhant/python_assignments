# 10.WAP to demonstrate the working of the following functions:
# i) read() 
# ii) read(n) 
# iii)readline() 
# iv) readlines() 

file = open("poem.txt","r")
print("file.read() function")
content=file.read() #this functions read whatever content there in the file and prints
print(content)

file.seek(0)
print('\n')

print("file.read(n) function")
content1= file.read(10) # reads the file until index n
print(content1)

file.seek(0)
print('\n')

print("file.readline() function")
content2=file.readline() #reads one single line
print(content2)

file.seek(0)
print('\n')

print("file.readlines() function") #file.readlines() returns a list where each line in the file is an element in that list.
content3 = file.readlines()
print(content3)

file.close()
