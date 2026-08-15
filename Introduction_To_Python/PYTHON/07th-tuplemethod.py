# We Know that we cannot modify tuple
"""In Build Method"""
#1.count()
#2.index()
"""In Build Function"""
# 1.len(tuple)
# 2.max(tuple)
# 3.min(tuple)
# 4.tuple(iterable)

fruits=("apple","banana","grapes","apple","Orange","apple")
#fruits="apple","banana","grapes","apple","Orange","apple" This is also a rule to write the tuple.Implicit Tuples
#print(fruits) 
#Nested_tuple=((10,20),(30,40),(50,60))
#print(Nested_tuple)
#print(Nested_tuple[0][1])
print(fruits.count("apple")) #In count method its count a item how many time exits in the tuple.
print(fruits.index("grapes")) #find the index number of the item in the tuple.
print(fruits.index("apple",2)) #find the index number of the item in the tuple starting index number from 2
print(fruits.index("apple",2,4)) #find the index number of the item in the tuple starting index number from 2 ending index number 4


numbers=(10,20,30,40)
x=max(numbers) #Print maximum number of the tuple.
y=min(numbers) #Print minimum number of the tuple,
z=len(numbers) #print length of the number.
print(x)
print(y)
print(z)

food=["Biriyani","Egg Roll","Chawmin","Moglai","Chiken Kosha","Fried rice"]
string="hello"
colors={"red","yellow"} #In this method its prints list,set,string into tuple
a=tuple(string)
t=tuple(food)
b=tuple(colors)
c=range(5)  #print range.
print(t)
print(a)
print(b)
print(c)
