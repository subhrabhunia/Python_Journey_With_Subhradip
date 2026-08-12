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