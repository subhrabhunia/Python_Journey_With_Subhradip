# SYNTAX:-
# def outer():   outer function
#     def inner():  inner function
#         Code Statement
#     inner()
#     outer()

#Basic Example
def outer():
    print("Inside Outer Function")
    def inner():
        print("Inside Inner Function")

    inner()
outer()

#Calculator
def calculator(a,b):
    def add():
        return a+b
    def substract():
            return a-b
    def multiplication():
            return a*b
    def divide():
            return a%b
    print("Addition:",add())
    print("Substraction:",substract())
    print("Multiplication:",multiplication())
    print("Divition:",divide())
calculator(20,5)