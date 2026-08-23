#SYNTAX OF NESTED STATEMENT
# if Condition1:
#     Statements
#    if Condition2:
#       Statements
# else:
#     Statement


#Voting System
User_Age=float(input("Enter Your Age:"))
User_Citizen=input("Enter Your Citizen:")
if User_Age>=18:
    if User_Citizen=="India":
        print("You are Eligable for vote")
    else:
        print("Must be a citizen Of India")
else:
    print("Must be at least 18 Years")

Age=float(input("Enter Your Age:"))
Have_Valid_Id=input("You Have Valid Id:")
if Age>=18:
    if Have_Valid_Id=="Yes":
        print("You are Eligable for vote")
    else:
        print("Must be Have a valid Id")
else:
    print("Must be at least 18 Years")


#ATM WITHDRAWL 
balance=15000
withdrawl=float(input("Enter Your Withdrawl Amount:"))
if balance>=withdrawl:
    if withdrawl<=10000:
        print("Transaction Succesfully")
    else:
        print("Withdrawl limit exceeded.Mximum Amount 10000")
else:
    print("You don't have sufficient balance.")


#Driving lincense Check
Driving_License=input("Enter You Have Driving Lincense(Yes/No):")
Driver_Age=float(input("Enter Your Age:"))
if Driving_License=="Yes":
    if Driver_Age>=18:
        print("You Can Go.")
    else:
        print("You Mast be 18 years old.You Get a Fine For This")
else:
    print("You Must Have Driving Licencse")