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