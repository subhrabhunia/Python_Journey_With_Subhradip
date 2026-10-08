Input1=int(input("Enter the first number: "))
Input2=int(input("Enter the second number: "))
Input3=int(input("Enter the third number: "))
if Input1>=Input2 and Input1>=Input3:
    print("The greatest number is:",Input1)
elif Input2>=Input1 and Input2>=Input3:
    print("The greatest number is:",Input2)
else:
    print("The greatest number is:",Input3)