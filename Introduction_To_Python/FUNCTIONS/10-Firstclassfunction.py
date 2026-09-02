# First-Class functions are those functions which can be passed as arguments to other functions, returned as values from other functions, and assigned to variables. In Python, functions are first-class citizens, meaning they can be treated like any other object.    
# Features of First-Class Functions:
# 1.Stored in variables
# 2. Passed as arguments to other functions
# 3. Returned from other functions
# 4.stored inside lista or dictionaries
# 5.Assigned to multiple variables

#Example
def greet():
    print("Hello")
message=greet  #Assigning function to a variable
message()  #Calling function using variable 
print(type(message))  # Output: <class 'function'>  

a=greet  #Assigning function to another variable
b=greet  #Assigning function to another variable
c=greet  #Assigning function to another variable
a()  #Calling function using variable a
b()  #Calling function using variable b
c()  #Calling function using variable c


#Stores funtion in a list
def add():
    print("Addition")
def sub():
    print("Subtraction")
def mul():
    print("Multiplication")
operations=[add,sub,mul]  #Storing functions in a list
for operation in operations:
    operation()  #Calling functions from the list
print(type(operations))  # Output: <class 'list'>
