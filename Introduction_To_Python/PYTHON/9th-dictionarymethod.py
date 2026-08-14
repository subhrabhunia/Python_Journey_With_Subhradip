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

