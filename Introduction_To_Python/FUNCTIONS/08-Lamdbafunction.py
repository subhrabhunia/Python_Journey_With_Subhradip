# This is a one line function which is defined using the keyword lambda. It can take any number of arguments, but can only have one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. You can use lambda functions when you require a nameless function for a short period of time.
# SYNTAX:-
# sum=lambda a,b:a+b
# print(sum(5,6)) # Output: 11
# Features of Lambda Functions:
# 1.has no function name (i.e. it is an anonymous function)
# 2.can take any number of arguments
# 3.is written in one line 
# 4.can contain only a single expression 
# 5.Automatically returns the value of the expression


#Basic Example
sum=lambda a,b:a+b
print (sum(10,20)) 
print (sum(13,20)) 

#Square
square=lambda x:x*x  #(x**2)
print(square(4))
print(square(5))

#Cube
cube=lambda y:y**3 #(y*y*y)
print(cube(2))
print(cube(3))

#Maximum of two numbers
maximum=lambda a,b:a if a>b else b
print(maximum(10,20))
print(maximum(30,20))

#Square every number in a list using lambda function using map() function
numbers=[1,2,3,4,5]
result=list(map(lambda x:x**2,numbers))  #map is a built-in function that applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
print(result)  # Output: [1, 4, 9, 16, 25]  

results=map(lambda x:x**3,numbers)  #map is a built-in function that applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator).
print(list(results))  # Output: [1, 8, 27, 64, 125]   