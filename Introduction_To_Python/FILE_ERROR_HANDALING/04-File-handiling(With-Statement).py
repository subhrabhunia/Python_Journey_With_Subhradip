#Basic Example
with open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "r") as file:
    print(file.read())


#Count number of lines
count = 0
with open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\Python.txt") as file1:
    for line in file1:
        count += 1
print("Total Lines:", count)