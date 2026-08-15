"""Different Types Of List Method"""
# 1.insert()
# 2.append()
# 3.count()
# 4.clear()
# 5.copy()
# 6.extend()
# 7.index()
# 8.pop()
# 9.remove()
# 10.reverse()
# 11.sort()

"""Different Types Of Universal List Method"""
# 1.len(list)
# 2.max(list)
# 3.min(list)
# 4.list(seq)

"""Example of list method"""

fruits=["Apple","Mango","Banana"]
fruits.append("Cherry") #In append add new item in last of the list and print a new list.
print(fruits)

cricketer=["Virat Kohli","MS Dhoni","Rohit Sharma"]
cricketer.insert(1,"Gautam Gambhir") #In insert we add new item in any position with help of index number of list.
cricketer.insert(0,"Hardik pandiya")
print(cricketer)

course=["HTML","CSS","JAVASCRIPT","C++"]
course.remove("C++") #In remove method we remove item from the list.
print(course)

subject=["DSA","WEBDESIGN","SOFTWARE ENGENERING","CLOUD COMPUTING"]
subject.pop(2) #In Pop method we remove the item from list using index number.If we don't gave any index number in backet then its remove the last item from the list
subject.pop()
print(subject)

name=["Soumya","Akash","Biswa"]
name.clear() #In this method Remove the all item from the list.
print(name)

bike=["NINJA","JAVA","UNICORN","GLAMOUR"]
bike.sort() #In this Sort method its organise the list in alphabetic order.A<B<C<D......<Z.In sort method its sorting the Capital letter first.
bike.sort(reverse=True) #in this its sort reverse means Z to A. 
print(bike)

student=["Ram","Shayam","Bristi","Riya"]
student.reverse() #In this method its reverse the list item and create new list.
print(student)

last_name=["Bhunia","Sau","Sahoo","Das"]
tittle=last_name.copy() #In this Copy method this list copy into a new list that name is tittle.
tittle=list(last_name) #It is also a copy method.
tittle=last_name[2:] #This is Also copy method but using index number if we print all item in the list then [:].If we want to print from index number 2 then [2:].If we want to print from index nuber 0 to 1 then [0:1] 
print(tittle)

Student=["Ram","Shayam","Lakshman"]
boy=["Subhradip","Sayan","Akash"]
Student.extend(boy) #In this method ww add the second list into first list and create the new list with the same name of first list. In extend method we also add the tuple into the list. All same process.
print(Student)

city=["Kolkata","Howraha","Delhi","Mumbai","Orrisa","Howraha"]
x=city.index("Delhi") #In this method we find the index number of the item from the list.If in the list the duplicate item present then it print first item's index number that found.
# x=city.index("India") if the item not present in list then show error.
# x=city.index("Howraha",2) If we want to print the last duplicate item name in the list then we gave the parameter number
# x=city.index("Howraha",2,6) last index number .
print(x)

x=city.count("Mumbai")  #In this method its count the values of the item means how many times its present in the list.
print(x)


"""UNIVERSAL METHOD EXAMPLE"""
food=["Biriyani","Egg Roll","Chawmin","Moglai","Chiken Kosha","Fried rice"]
numbers=[10,20,30,40,50,60]
c=len(food) #In this method this print total length of the list means how many items present in the list.
x=max(food) #In this method its maximum if the string value then it give the alphabetic order.If numeric then
y=max(numbers) #the Largest number of the list
d=min(food) #This is Alphabaticly 
e=min(numbers) #This print Smallest number of the list.
print(d)
print("Minimum:",e)
print(y)
print(x)
print (c)

Colors_Numbers=("Black","Green","White",1,2,3,)
Colors_list= list(Colors_Numbers) #In this method we convert tuple,set,string values into the list.
print(Colors_list)
