# palindrome method is used to check if a string or number reads the same backward as forward. In Python, you can check if a list contains a palindrome by iterating through the list and checking each element. Here's an example code snippet that demonstrates how to do this: 
List1=[1,2,1]
Lis2=[1.2,3]
copy_list1=List1.copy()
copy_list1.reverse()
if copy_list1==List1:
    print("List1 contains a palindrome.")
else:
    print("List1 does not contain a palindrome.")

copy_list2=Lis2.copy()
copy_list2.reverse()
if copy_list2==Lis2:
    print("Lis2 contains a palindrome.")
else:
    print("Lis2 does not contain a palindrome.")