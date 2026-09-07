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

#Generic Reusable decorater
def decorator(function):
    def wrapper(*args,**kwargs):
        print("Starting....")
        result = function(*args,**kwargs)
        print("Finished")
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))

#Login check decorator
def login_required(func):
    def wrapper():
        logged_in = True  

        if logged_in:
            func()
        else:
            print("Please login first")

    return wrapper


@login_required
def dashboard():
    print("Welcome to Dashboard")


dashboard()


#Use Multiple decorator

def star(func):
    def wrapper():
        print("************")
        func()
        print("************")
    return wrapper


def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper


def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


@star
@decorator1
@decorator2
def hello():
    print("Hello")


hello()