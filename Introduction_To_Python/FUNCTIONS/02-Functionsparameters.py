#Example1
def hello(fname,lastname):
    print("Hello",fname,lastname)
hello("Subhradip","Bhunia")
print("_____________________")


#fuction with parameters
def sum(a=10,b=20):  #we assign default value.
    print(a+b)
sum(10,20)
print("_____________________")
sum(40,20)
print("_____________________")
sum(10,90)
print("_____________________")
sum(50,60)
print("_____________________")
sum(70,30)
print("_____________________")


#fuction with  multipy parameters
def multypy(A,B):
    result=(A*B)
    print("Multiplication:",result)
multypy(10,20)
print("_____________________")
multypy(40,20)
print("_____________________")
multypy(10,90)
print("_____________________")
multypy(50,60)
print("_____________________")
multypy(30,30)
print("_____________________")

#fuction with Division parameters
def division(c,d):
    results=(c%d)
    print("Division:",results)

first=float(input("Enter First Number:"))
second=float(input("Enter Second Number:"))
division(first,second)
print("_____________________")

#keyword argument
def hello(Firstname,Lastname,age,city):
    print("Hello",Firstname,Lastname,age,city)
hello("Subhradip","Bhunia",city="kolkata",age=20)
print("_____________________")


# / — Positional-only arguments
# Arguments before / must be passed by position.
# * — Keyword-only arguments
def student(name, age, /):
    print(name, age)

student("Rahul", 20)       # ✅
student(name="Rahul", age=20)  # ❌

# * — Keyword-only arguments
# Arguments after * must be passed using their names.
def student(name, *, age):
    print(name, age)

student("Rahul", age=20)   # ✅
student("Rahul", 20)       # ❌