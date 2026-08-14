"""KEY POINTS OF SET"""
# 1.stores unique values only.
# 2.duplicate values are automatically removed.
# 3.Unordered(no indexing)
# 4.Mutable(can add/remove items).
# 5.Can contain different data types.

"""SET IN BUILD METHOD"""
# 1.add()
# 2.update()
# 3.remove()
# 4.discard()
# 6.pop()
# 7.clear()
# 8.copy()

fruits={"apple","banana","orange"}
print(fruits)
print(type(fruits))


fruits.add("cherry") #How to add any value on set
print(fruits)

more_fruits={"guava","pineapple"} #How to update item in set.
fruits.update(more_fruits)
print(fruits)

other_fruits=["pear","lime"]
fruits.update(other_fruits)  #How to add list in set.
print(fruits)

fruits.remove("apple") #How to remove an item from set.
print(fruits)

fruits.discard("lichi") #its any item not present in liat then we rongly type the item then this not give error.
print(fruits)

fruits.pop()  #Its delete random value from set.
print(fruits)

item=fruits.pop()  #Its delete random value from set.
print(item) #if we want to see what item delete from set
print(fruits)

new_fruits=fruits.copy()  #How to create a copy of the set.
print(new_fruits)

for item in fruits:  #how to print all value.
    print(item)


print("banana"in fruits)  #how to check any value is present in set.
print("mango"in fruits)  #If any value not present in set.


numbers={10,20,30,10,20}
print(numbers)  #set not print duplicate value.

data={10,"Hello",4.5,True}  #set print all types of data types.
print(data)

name=set() #how to create empty set.
print(type(name))

fruits.clear() #Its clear all item from set.
print(fruits)