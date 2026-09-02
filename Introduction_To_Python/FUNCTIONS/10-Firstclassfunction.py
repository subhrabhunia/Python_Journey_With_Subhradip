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