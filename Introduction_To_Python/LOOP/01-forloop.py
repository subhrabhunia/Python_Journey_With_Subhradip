# SYNTAX OF FOR LOOP:
# for variable in sequence:
#     #Code to execute

# which we use for loop
# 1.list
# 2.tuple
# 3.String
# 4.dictionary
# 5.set
# 6.range of numbers


#Example
x=["HTML","CSS","JS","Python","MySQL"]
for subject in x:
    print(subject)

#List example
fruits=["Apple","Guava","Orange",'Banana']
for fruit in fruits:
    print(fruit)

#Tuple Example
Names=("Subhra","Soumya","Akash","Biswajit")
for name in Names:
    print(name)

#Set Example
Girls={"Riya","Sita","Mou","Mita"}
for girl in Girls:
    print(girl)

#String Example
subject="Python"
for letter in subject:
    print(letter)

#Dictionary Example
student={
    "Name":"Subhradip",
    "Age": 22,
    "Course":"Python"
}
for key,value in student.items():
    print(key,":",value)

#Enumerate Function
students=["Ram","Sita","Lakshman","Riya"]   #Print index number.It also working with tuple list.
for index,students in enumerate(students):
    print(index,":",students)

#Enumereate with string
y="FULL StACK"
for indexes,character in enumerate(y):
    print(indexes,":",character) 

#zip method
phone_brand=["VIVO","REALME","REDMI","IPHONE"]
rate=[35000,40000,45000,50000]
for brand,rates in zip(phone_brand,rate):
    print(brand,"Rate is:",rates)      #Its working when two key have same number values.

#Range Example
for i in range(5):
    print(i)

for j in range(2,15):
    print(j)  #Its started print from 2

for k in range(2,15,2):   #Start point end point step
    print(k)  #Itsw step 2.

for l in range (10,0,-1):
    print(l)   #Its working in reverse

#even check
for num in range(1,11):
    if num%2==0:
        print(num)

#odd check
for nums in range(1,11):
    if nums%2!=0:
        print(nums)

#Multiplication Table
for number in range (1,11):
    print("2 x",number,"=",2*number)

for numbers in range (1,11):
    print(f"3 X {numbers} = {3*numbers}")

#or else statement
for Number in range(1,6):
    print(Number)
else:
    print("Loop Completed.")