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
