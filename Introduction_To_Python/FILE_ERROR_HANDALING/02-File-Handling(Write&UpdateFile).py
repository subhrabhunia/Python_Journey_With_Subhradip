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
file.close()