"""DICTIONARY METHODS"""
# 1.get()
# 2.values()
# 3.keys()
# 4.items()
# 5.fromkeys()
# 6.pop()
# 7.popitem()
# 8.clear()
# 9.update()
# 10.copy()
# 11.setdefault()

"""IN BUILD METHOD"""
# 1.len(dict)
# 2.str(dict)


student={
    "name":"Subhradip",
    "age":20
}

print(student.get("name")) #In get method we print the output that i want.
print(student.get("city","Not Found"))  #It's print none beacuse city name varriable not avilabe.If we want custome message then add "zcustom message".

print(student.keys()) #It's shows all keys.
print(list(student.keys()))  #If we want to show all keys in a list.

print(student.items()) #It creates a list under the list create tuple under first tuple it store it first keys and first values and second tuple store second keys and second value.

for key, value in student.items():
    print(key,":",value)  #Like the items method difference is using for loop.

keys=["name","age","city"]
data=dict.fromkeys(keys,"Unknown") #Using fromkeys its create a dictionary and give values automatically."Unknown" use to default message.
print(data)

# student.pop("age") #its uses to remove what key i want to delete.
# print(student)
age=student.pop("age")
print(age)

print(student.popitem()) #Its remove the last key.

student.clear()
print(student) #It's  remove all keys.

student.update({"city":"delhi"}) #its use to update or add the key and value in dictionary.
student.update({"age":25})
student.update(name="Soumya")
print(student)

new_student=student.copy() #It's uses to copy the list.
print(new_student)


print(student.setdefault("name"))  #it uses to give the value of the key.
print(student.setdefault("gender","UNKNOWN")) #print default value.
print(student)


