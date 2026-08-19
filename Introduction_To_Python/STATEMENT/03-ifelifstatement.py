# In ifelif statement we check the the many condition .
#SYNTAX OF IF ELIF STATEMENT
# if Condition:
#     Statement
# elif Condition:
#     Statement
# else:
#     Statement


#Reallife Example:
User_Name=input("Enter Your Name:")
Percentage=float(input("Enter the Percentage:"))

if Percentage>=80 and Percentage<=100:
    print(User_Name,"You Are Pass in Merit list")
elif Percentage>=60 and Percentage<=79:
    print(User_Name,"You Are Pass in 1st Division")
elif Percentage>=45 and Percentage<=59:
    print(User_Name,"You Are Pass in 2nd Division")
elif Percentage>=33 and Percentage<=44:
    print(User_Name,"You Are Pass in 3rd Division")
elif Percentage<33:
    print(User_Name,"You Are Fail")
else:
    print(User_Name,"Enter the correct Percentage")



Name = input("Enter Your Name: ")
Age = int(input("Enter Your Age: "))

if Age >= 0 and Age <= 3:
    print(Name, "You Are A Baby")
elif Age >= 4 and Age <= 12:
    print(Name, "You Are A Child")
elif Age >= 13 and Age <= 19:
    print(Name, "You Are A Teenager")
elif Age >= 20 and Age <= 59:
    print(Name, "You Are An Adult")
elif Age >= 60:
    print(Name, "You Are A Senior Citizen")
else:
    print("Enter a valid age")


user_Name = input("Enter Your User_Name: ")

Password = int(input("Enter Your Password: "))

if user_Name != "Admin":
    print("Invalid User Name")

elif Password != 1234:
    print("Invalid Password")

else:
    print("Log in Successfull")