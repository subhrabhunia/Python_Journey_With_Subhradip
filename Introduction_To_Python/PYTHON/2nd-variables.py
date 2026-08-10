A="Hello World!" #A variable named A is created and assigned the string value "Hello World!". In Python, variables are used to store data values, and they can be assigned using the equal sign (=). The variable name can be any valid identifier, and it is case-sensitive.   
print(A) #The above line prints the value of the variable A, which is "Hello World!". The print function is used to display output in Python.   
print(A)
print(A) #print the varriable A three times. The print function is called three times, and each time it prints the value of the variable A, which is "Hello World!".if any change Hello world! is made in the variable A, it will be reflected in all the three print statements. This is because the variable A holds a reference to the string value "Hello World!", and when we print the variable, we are accessing that reference. If we change the value of A, the reference will point to the new value, and all subsequent print statements will reflect that change.

"""Variables Example:-"""
Name="Subhradip" #This is String value.A variable named Name is created and assigned the string value "Subhradip". In Python, variables are used to store data values, and they can be assigned using the equal sign (=). The variable name can be any valid identifier, and it is case-sensitive.
Age=20 #This is Nuemeric Valus.A variable named Age is created and assigned the integer value 20. In Python, variables can hold different data types, including integers, strings, floats, and more. The variable name can be any valid identifier, and it is case-sensitive.
height=5.6 #This is Float Value.A variable named height is created and assigned the float value 5.6. In Python, variables can hold different data types, including integers, strings, floats, and more. The variable name can be any valid identifier, and it is case-sensitive.
print("My Name is :",Name)
print("And My age is :",Age)
print("And My height is :",height) #The above line prints the string "My Name is :" followed by the value of the variable Name, then the string "And My age is :" followed by the value of the variable Age, and finally the string "And My height is :" followed by the value of the variable height. The comma (,) is used to separate multiple items in the print function, and it automatically adds a space between them when printed. 

"""Variables Example:-"""
#second varriables are print below because the first varriables are changed in the above code. The new values of the variables Name, Age, and height are assigned, and when we print them again, they will reflect the new values. This demonstrates that variables can be reassigned to hold different values during the execution of a program.
Name="Subhradip" 
Age=20 
height=5.6 

Name="Soumya"
Age=21
height=5.7
print("My Name is "+Name+", And My age is "+str(Age)+", And My height is "+str(height)) #The above line prints the string "My Name is" followed by the value of the variable Name, then the string "And My age is" followed by the value of the variable Age, and finally the string "And My height is" followed by the value of the variable height. The plus (+) operator is used to concatenate strings in Python, and we can convert non-string values to strings using the str() function.
# print("My Name is :",Name)
# print("And My age is :",Age)
# print("And My height is :",height)


a,b,c="orange","banana","cherry" #This is also the right way to define multiple variables in a single line in Python. The variables a, b, and c are assigned the string values "orange", "banana", and "cherry" respectively. This is a common convention in Python for defining multiple variables in a single line.
print(a) #The above line prints the value of the variable a, which is "orange". The print function is used to display output in Python.
print(b) #The above line prints the value of the variable b, which is "banana". The print function is used to display output in Python.
print(c) #The above line prints the value of the variable c, which is "cherry". The print function is used to display output in Python.


x=y=z="orange" #This is also the right way to define multiple variables in a single line in Python. The variables x, y, and z are all assigned the string value "orange". This is a common convention in Python for defining multiple variables in a single line.
print(x) #The above line prints the value of the variable x, which is "orange". The print function is used to display output in Python.
print(y) #The above line prints the value of the variable y, which is "orange". The print function is used to display output in Python.
print(z) #The above line prints the value of the variable z, which is "orange". The print function is used to display output in Python. 

"""Right Way To Define Variables:-
FirstName="Subhradip" #This is the right way to define a variable in Python. The variable name starts with a letter and uses camel case notation, where the first letter of each word is capitalized except for the first word. This makes the variable name more readable and easier to understand."
First_Name="Subhradip" #This is also the right way to define a variable in Python. The variable name starts with a letter and uses underscores to separate words. This makes the variable name more readable and easier to understand."
firstname="Subhradip" #This is also the right way to define a variable in Python. The variable name starts with a letter and uses all lowercase letters. This is a common convention in Python for variable names."
firstname1="Subhradip" #This is also the right way to define a variable in Python. The variable name starts with a letter and uses all lowercase letters, followed by a number. This is a common convention in Python for variable names.
a,b,c=10,20,30 #This is also the right way to define multiple variables in a single line in Python. The variables a, b, and c are assigned the values 10, 20, and 30 respectively. This is a common convention in Python for defining multiple variables in a single line.
x=y=z=10 #This is also the right way to define multiple variables in a single line in Python. The variables x, y, and z are all assigned the value 10. This is a common convention in Python for defining multiple variables in a single line."""


"""Wrong Way To Define Variables:-
1. 1stName="Subhradip" #This is the wrong way to define a variable in Python. The variable name starts with a number, which is not allowed in Python. Variable names must start with a letter or an underscore.
2. First-Name="Subhradip" #This is the wrong way to define a variable in Python. The variable name contains a hyphen (-), which is not allowed in Python. Variable names can only contain letters, numbers, and underscores.
3. First Name="Subhradip" #This is the wrong way to define a variable in Python. The variable name contains a space, which is not allowed in Python. Variable names can only contain letters, numbers, and underscores.
4. First@Name="Subhradip" #This is the wrong way to define a variable in Python. The variable name contains a special character (@), which is not allowed in Python. Variable names can only contain letters, numbers, and underscores.
5. First#Name="Subhradip" #This is the wrong way to define a variable in Python. The variable name contains a special character (#), which is not allowed in Python. Variable names can only contain letters, numbers, and underscores.
6. First$Name="Subhradip" #This is the wrong way to define a variable in Python. The variable name contains a special character ($), which is not allowed in Python. Variable names can only contain letters, numbers, and underscores.
7. First%Name="Subhradip" #This is the wrong way to define a variable in Python. The variable name contains a special character (%), which is not allowed in Python. Variable names can only contain letters, numbers, and underscores.
8. First^Name="Subhradip" #This is the wrong way to define a variable in Python. The variable name contains a special character (^), which is not allowed in Python. Variable names can only contain letters, numbers, and underscores."""