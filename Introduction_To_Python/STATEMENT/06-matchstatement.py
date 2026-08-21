# SYNTAX OF MATCH STATEMENT
# case pattern1:
#     Code Block 
# case pattern2:
#     Code Block  
# case_:
#     Default Code Block  
# Its like Switch Case Statement.


# IT CAN MATCH:
# 1.Exact values.
# 2.Multiple values.
# 3.Varriables.
# 4.Lists and tuples.
# 5.Dictionaries.
# 6.Conditions(using guards).

#Week-Days Example
Date=int(input("Enter The Number of the Day:"))
match Date:
    case 1:
        print("It Is Monday")
    case 2:
        print("It Is Tuesday")
    case 3:
        print("It Is Wednesday")
    case 4:
        print("It Is Thurshday")
    case 5:
        print("It Is Friday")
    case 6:
        print("It Is Saturday")
    case 7:
        print("It Is Sunday")
    case _:
        print("Enter Correct Day")

#Calculator
Number1=float(input("Enter the First Number:"))
Number2=float(input("Enter the Second Number:"))
operator=input("What can You Do give that Symbol:")
match operator:
    case"+":
        print(Number1+Number2)
    case"-":
        print(Number1-Number2)
    case"*":
        print(Number1*Number2)
    case"/":
        print(Number1/Number2)
    case"%":
        print(Number1%Number2)
    case _:
        print("Invlid Operator")


Date=int(input("Enter The Number of the Day:"))
match Date:
    case 1:
        print("It Is Monday")
    case 2:
        print("It Is Tuesday")
    case 3:
        print("It Is Wednesday")
    case 4:
        print("It Is Thurshday")
    case 5:
        print("It Is Friday")
    case 6|7:  #OR operator in match
        print("It Is Weekend")
    case _:
        print("Enter Correct Day")

#Month-Season 
Month=input("Enter The Month Name:")
match Month:
    case "December"|"January"|"February":
        print("It Is Winter")
    case "March"|"April"|"May":
        print("It Is Spring")
    case "June"|"July"|"August":
        print("It Is Summer")
    case"September"| "October"|" November":
        print("It Is Autumn/Fall")
    case _:
        print("Enter Correct Month")


#Match list
list=[10,20]
match list:
    case[10,20]:
        print("Both Number found")
    case[10]:
        print("Only first number found")
    case[20]:
        print("Only second number found")
    case _:
        print("No number found")

#Match tuple
tuple=(5,8)
match tuple:
    case(0,0):
        print("Origin")
    case(0,y):
        print("Y axis:",y)
    case(x,0):
        print("X Axis:",x)
    case _:
        print("Unknown Tuple")


#Dictionary match
student={
    "Name":"Subhradip",
    "Age":21
}
match student:
    case{"Name":Name,"Age":Age}:
        print(Name)
        print(Age)
    case _:
        print("Invalid data")


#if statement
Age_1=float(input("Enter your age:"))
match Age_1:
    case x if x<=13:
        print("child")
    case x if x <=20:
        print("Teenger")
    case x if x <=60:
        print("Adult")
    case _:
        print("Senior Citizen")

#Wild card
point=(10,20)
match point:
    case(_,20):
        print("Second Value is 20")
    case _:
        print("No match")