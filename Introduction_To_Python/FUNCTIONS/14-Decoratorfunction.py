# Input Function
#       |
#       |
#       v
# def decorator(function):
#       |
#       |  Extra code / behavior
#       |
#       v
# Output Function
# (with Extra Behavior)

# SYNTAX:-
# def decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
    
#     return wrapper


# @decorator
# def hello():
#     print("Hello World")


# hello()

# Flow:-
# @decorator
#     ↓
# hello function
#     ↓
# decorator(hello)
#     ↓
# wrapper function
#     ↓
# hello()
#     ↓
# Before
# Hello World
# After

# Real Use Case of decorator:
# 1.Log messages
# 2.Check Login
# 3.Check Permission
# 4.Calculate execution time

#Basic Example
def decorator(func):
    def wrapper():
         print("Before")
         func()
         print("After")
    
    return wrapper


@decorator
def hello():
     print("Hello World")

hello()

#Second method
def decorators(function):
    def wrappers():
         print("Before")
         function()
         print("After")
    
    return wrappers

def hello():
     print("Hello Worlds")
test=decorators(hello)
test()

#Decorator with arguments
def decorator1(functions):
    def wrapper(name):
        print("Before")
        functions(name)
        print("After")

    return wrapper


@decorator1
def hello(name):
    print(f"Hello {name}")


hello("Subhradip")