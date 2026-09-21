#Basic Example
with open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "r") as file:
    print(file.read())


#Count number of lines
count = 0
with open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\Python.txt") as file1:
    for line in file1:
        count += 1
print("Total Lines:", count)

#Write Example
with open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "w") as file:
    file.write("RAM\n")
    file.write("Shayam\n")
    file.write("Jodhu")
print("File Written Successfully.")

#Append File-Notes as a application
student=input("Enter a student name:")
with open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "a") as file:
    file.write(student+ "\n")
print("Saved name Successfully")

#Copy method
with open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "r") as source:
    content=source.read

with open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\newfile.txt", "w") as destination:
    destination.write(content)
print("File Copied")

