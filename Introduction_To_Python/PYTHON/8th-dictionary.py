# KEY POINTS OF DICTIONARY:
# 1.Keys must be unique.
# 2.Keys can be string,numbers,tuples,etc.
# 3.Values can be of any data type.
# 4.Dictionaries are mutable(changeable)
# 5.Access values using keys.

student={ 
    "name":"John",
    "age":20,
    "city":"Kolkata"
    }

student["gender"]="male" #If we want to any new key value in the dictionary.

student["age"]=21 #If we want to change any key name or value.

print(student) #This print all values of dictionary.
print(type(student)) #This print all the values.  
print(student["name"]) #if we want to see any one key value.This print name.  
print(student["age"]) #This print age.
print(student["city"]) #This print city.