"""THIS IS I GIVE THE INPUT AND OUTPUT IN CODE AND PYTHON PRINT IT"""
name="Subhradip"
city="Kolkata"

print("Hello My Name Is:",name)
print("My City Is:", city)


"""THIS I GIVE THE INPUT IN TERMINAL THEN IT PRINTS THE OUTPUT(USER GIVE THE INPUT TO SOFTWARE)"""
Name=input("")
City=input("")

print("Hello My Name Is:",Name)
print("My City Is:", City)


"""Print with message"""
Name=input("Enter your Name:")   #Using for string
City=input("Enter Your City:")

print("Hello My Name Is:",Name)
print("My City Is:", City)

print("Hello My Name Is:",Name, end= " ")  #using end print output in one line
print("My City Is:", City)


print(f"My name is {Name} and City is {City}")  #print output one line with using formated string.


"""ARITHMETIC CALCULATION"""
width=int(input("Enter Width:"))
height=int(input("Enter Height:"))  #for numerical we use int.

area=width*height

print("Area of the room is:",area)

number1=float(input("Enter Number1:"))
number2=float(input("Enter number2:"))  #for floating number.

maltiplication=number1*number2

print("The Maltiplication of two number:",maltiplication)


"""EROR HANDALING"""
try:                    #Use this for error handaling
    width1=int(input("Enter Width:"))
    height2=int(input("Enter Height:"))
except ValueError: 
    print("please enter a valid number")
area1=width1*height2

print("Area of the room is:",area1)