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
