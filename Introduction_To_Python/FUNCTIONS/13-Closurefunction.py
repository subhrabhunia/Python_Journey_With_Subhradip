# SYNTAX:-
# def outer_function():
#     x = 10
#     def inner_function():      This is a closure function because it is defined inside another function and has access to the variables of the outer function.
#         print("Value of x:", x)
#     return inner_function
# test_closure = outer_function()
# test_closure()  # Output: Value of x: 10

# WHY WE USE CLOSURE FUNCTION?
# Closure functions are used for several reasons:
#     1.Remember some data: Closure functions can remember the values of variables from their enclosing scope, even after the outer function has finished executing. This allows them to maintain state and retain information across multiple calls.
#     2.Hide internal variables: Closure functions can encapsulate and hide internal variables from the global scope, providing a way to create private variables and functions.
#     3.Create customized functions: Closure functions can be used to create specialized functions that are tailored to specific needs, allowing for more flexible and reusable code. 
#     4.Maintain state without using classes: Closure functions can be used to maintain state without the need for creating classes, making them a lightweight alternative for certain scenarios. 


#Basic Example of closure function
def outer_function():
    message = "Hello, World!"
    def inner_function():
        print(message)  
    return inner_function
test_closure = outer_function()
test_closure()  # Output: Hello, World!

#Closure function with parameters
def greeting(name):
    def say_hello():
        print(f"Hello, {name}!")
    return say_hello
person1= greeting("Alice")
person2=greeting("Bob")
person1()  # Output: Hello, Alice!
person2()  # Output: Hello, Bob!

