"""Check whether a values exits inside a collection"""
# 1.List
# 2.Tuple 
# 3.Set 
# 4.Dictionary
# 5.String 


# | Operator | Description                                             | Example              | Result |
# | -------- | ------------------------------------------------------- | -------------------- | ------ |
# | `in`     | Returns `True` if a value exists in a sequence.         | `"a" in "apple"`     | `True` |
# | `not in` | Returns `True` if a value does not exist in a sequence. | `"z" not in "apple"` | `True` |


numbers=[20,30,10,40]   #is is in list or tuples,set,dictionary
print(20 in numbers)#True
print(100 in numbers) #False
print(80 not in numbers) #true
print(10 not in numbers) #False

fruits = ["apple", "banana", "mango"]
print("apple" in fruits)      # True
print("orange" in fruits)     # False
print("orange" not in fruits) # True


text="Python Programming"
print("Python" in text)
print("Java" in text)

student={
    "name":"John",
    "age":20
}
print("name" in student)
print("John" in student)  #its print False because Its check the keys not values.



#Real Life Example
# if a software is image extensions storing website then  
allowed_Extension=[".jpg",".png",".gif"]
filename="Photo.png"
if ".png" in filename:
    print("Image accepted")