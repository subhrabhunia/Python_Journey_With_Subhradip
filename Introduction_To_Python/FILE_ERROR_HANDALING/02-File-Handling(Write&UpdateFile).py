#Create and Write File
file = open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "w")
file.write("Hello Python Developr\n")
file.write("Subhradip\n")
file.write("Soumya\n")
file.write("Ram\n")

#Writee lines
names=[
    "Jodhu\n",
    "Modhu\n",
    "Shayam\n"
]
file.writelines(names)

#Append Mode
file = open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "a")
file.write("Riya")

#Read and write mode
file = open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "r+")
print(file.read())
file.write("\nPython")

#Write and Read Mode
file = open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "w+")
file.write("\nHtml")
file.seek(0)
print(file.read())

#Append and Read mode
file = open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\File.txt", "a+")
file.write("\nJava")
file.seek(0)
print(file.read())

#create mode x
file = open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\New.txt", "x")  #To create a new file
file.write("Html\n")
file.write("Java\n")
file.close()