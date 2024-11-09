# 9. Write a program to write “Happy Programming” in a text file and read it
file= open("message.txt", "w")
file.write("Happy Programming")
file.close()


file1=open("message.txt", "r") 
content = file1.read()

print("Content of the file:", content)

