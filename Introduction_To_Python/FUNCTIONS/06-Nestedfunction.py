# SYNTAX:-
# def outer():   outer function
#     def inner():  inner function
#         Code Statement
#     inner()
#     outer()

#Basic Example
def outer():
    print("Inside Outer Function")

    message="welcome"
    
    def inner():
        print("Inside Inner Function")
        print(message) #We can print this in inner function.

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

#Login System
def login(username,password):
      def validate():
            return username=="admin" and password=="1234"
      if validate():
            print("Login Sucessful")
      else:
            print("Invalid Credentials")
username=input("Enter UserName:")
password=input("Enter Password:")
login(username,password)