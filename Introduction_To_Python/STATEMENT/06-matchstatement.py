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

