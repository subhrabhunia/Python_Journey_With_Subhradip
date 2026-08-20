#SYNTAX OF CONDITIONAL EXPRESSION (others name is ternary operator.)
#varriable=value_if_True if condition else value_if_false


#USer age check
age=float(input("Enter Your Age:"))
Status="Adult" if age>=18 else "Minor"
print(Status)


#Ever or odd
number=float(input("Enter a number:"))
Result= "Even" if number %2 else "Odd"
print(Result)

#Marks check
marks=float(input("Enter a Your number:"))
result=(
    "A" if marks>=90 else
    "B" if marks>=60 else 
    "C" if marks>=40 else 
    "FAILS")
print(result)