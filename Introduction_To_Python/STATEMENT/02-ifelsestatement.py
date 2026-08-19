# If-Else statement use to check the condition of a code,Its can give the results True or False,If the result is True then give a special statement and if condilions output is False then it also give a constatement.
# SYNTAX OF IF STATEMENT
#if condition:
#   Statements for True.
#else:
#  Stament for False.


# Real-Life Example
User_Age= float(input("Enter Your Age:"))
if User_Age>=18:
    print("You are Eligable for Vote")
else:
    print("You are Not Eligablbe for vote")


Number= float(input("Enter Your Number:"))
if Number>=0:
    print("The Number is Positive")
else:
    print("The Number is Negative")

Numbers=[10,20,30,40,50]
if 60 in Numbers:
    print("Present")
else:
    print("Not Present")


Name=input("Enter Your Name:")
Gender=input("Enter Your Gender:")
if (Gender=="Male"):
    print("Hello Mr.",Name)
else:
    print("Hello Miss.",Name)

User_Name=input("Enter Your User_Name:")
Password=int(input("Enter Your Password:"))
if (User_Name=="Admin" and Password==1234):
    print("Log in Successfully")
else:
    print("Invalid User Name or Password")