# Question 1
# What will be the output of the Python expression print("Hello" * 2 + "World")?
print("Hello"*2+"world")
# Answer="HelloHelloworld" because the asterisk operator repeats the string "Hello" twice without spacs,and the plus operator concatenates "world" to the end.


# Question 2
# Which of the following is a valid variable name according to Python naming rules?
# A.First-Name
# B.First_Name
# C.1stName
# D.First Name
# Answer=B.First_Name because Variable names in Python can start with letters or underscores and contain letters, numbers, and underscores.


# Question 3
# Given x = ["HTML", "CSS", "JavaScript", "Python"], what does print(x[0:2]) evaluate to?
x=["HTML","CSS","JavaScript","Python"]
print(x[0:2])
# Answer=["HTML", "CSS"] Slicing [start:end] starts at index 0 (inclusive) and ends at index 2 (exclusive), returning elements at index 0 and 1.


# Question 4
# What is the primary difference between remove() and discard() when removing an item from a Python set?
# Answer=remove() raises a KeyError if missing while discard() does nothing.The remove() method raises an exception if the specified element is not present, whereas discard() safely ignores missing elements.


# Question 5
# Consider data = [10, "Soumya", 35.5, True] followed by age, name, marks, married = data. What is the value of marks?
data=[10, "Soumya", 35.5, True]
age, name, marks, married = data
print(marks)
# Answer=35.5(Sequence unpacking maps list elements positionally; index 2 (35.5) maps directly to the third variable marks.)


# Question 6
# Given student = {"name": "Subhradip", "age": 20}, what will print(student.get("city", "Not Found")) output?
student = {"name": "Subhradip", "age": 20}
print(student.get("city", "Not Found"))
# Answer="Not Found"The get() method returns the specified fallback argument ("Not Found") when the key "city" does not exist in the dictionary.


# Question 7
# Given x = ("HTML", "CSS") and sir = ("Subhradip", "Soumya"), what happens when executing mix = x + sir?
x = ("HTML", "CSS")
sir = ("Subhradip", "Soumya")
mix=x+sir
print(mix)
# Answer=("HTML", "CSS", "Subhradip", "Soumya").The + operator concatenates two tuples into a new single tuple containing all elements in order.


# Question 8
#What will be printed by numbers = {10, 20, 30, 10, 20} followed by print(numbers)?
numbers={10,20,30,10,20}
print(numbers)
#Answer={10, 20, 30}.Python sets automatically eliminate duplicate elements, leaving only unique values.


#Question 9
#If keys = ["name", "age", "city"] and data = dict.fromkeys(keys, "Unknown"), what is data["age"]?
keys = ["name", "age", "city"]
data = dict.fromkeys(keys, "Unknown")
print(data["age"])
#Answer="Unknown"(dict.fromkeys() initializes all keys in the iterable with the specified default value ("Unknown").)


# Question 10
# Given cricketer = ["Virat Kohli", "MS Dhoni", "Rohit Sharma"], what is at index 1 after cricketer.insert(1, "Gautam Gambhir")?
cricketer = ["Virat Kohli", "MS Dhoni", "Rohit Sharma"]
cricketer.insert(1, "Gautam Gambhir")
print(cricketer)
#Answer="Gautam Gambhir"(['Virat Kohli', 'Gautam Gambhir', 'MS Dhoni', 'Rohit Sharma'])The insert(index, element) method places the new element exactly at the specified index, shifting remaining elements to the right.


# Question 11
#Given two sets A = {1, 2, 3} and B = {3, 4, 5}, what is the output of the expression A ^ B (or A.symmetric_difference(B))?
A = {1, 2, 3}
B = {3, 4, 5}
print(A^B)
print(A.symmetric_difference(B))
#Answer={1, 2, 4, 5}.Symmetric difference returns a set of elements that are in either of the sets, but not in both.


# Question 12
# Given E = {8, 9} and F = {2, 3}, what does the method call E.isdisjoint(F) return?
E={8,9}
F={2,3}
print(E.isdisjoint(F))
#Answer=True.isdisjoint() evaluates to True when two sets share no common elements.


# Question 13
# What is printed to the console when executing print('Hello My Name Is: Subhradip', end=' ') followed by print('My City Is: Kolkata')?
print('Hello My Name Is: Subhradip', end=' ')
print('My City Is: Kolkata')
#Answer="Hello My Name Is: Subhradip My City Is: Kolkata".Specifying end=' ' replaces the standard newline character with a single space, placing both print outputs on one line.


#Question 14
#If input1 = input() receives user entry "5" and input2 = input() receives user entry "4", what happens when executing print(input1 * input2)?
# input1 = input()
# input2 = input() 
# print(input1*input2)
#Answer=TypeError.In Python, using the * operator between two string operands triggers a TypeError because string repetition requires an integer multiplier.


# Question 5
# What will be printed when executing the following error handling snippet?
# try:
# width = int("20px")
# height = int("10")
# except ValueError:
# width = 0
# height = 0
# print(width + height)
# Answer=0
# Attempting int("20px") raises a ValueError, causing execution to jump to the except block where both variables are set to 0.


# Question 16
# Given variables name = "Soumya" and age = 21, what is the output of print(f"Name: {name}, Age: {age + 1}")?
name = "Soumya" 
age = 21
print(f"Name: {name}, Age: {age + 1}")
#Answer="Name: Soumya, Age: 22".F-strings evaluate expressions contained within curly braces, substituting name with "Soumya" and age + 1 with 22.


# Question 7
# Given student = {"name": "Subhradip", "age": 20}, what is returned by student.setdefault("city", "Kolkata")?
student = {"name": "Subhradip", "age": 20}
student.setdefault("city", "Kolkata")
print(student)
#Answer="Kolkata".{'name': 'Subhradip', 'age': 20, 'city': 'Kolkata'}.When the requested key is missing from the dictionary, setdefault() inserts the key with the provided default value and returns that value.


# Question 18
# What is the primary difference between s.discard(40) and s.remove(40) when 40 is not present in set s?
# Answer=discard() performs no operation while remove() raises a KeyError..discard() removes an element if present and suppresses errors if absent, whereas remove() raises a KeyError when the element is not in the set.


# Question 19
# Given data = [10, "Soumya", 35.5, True], what is the value and structure assigned to rest after executing age, name, *rest = data?
data = [10, "Soumya", 35.5, True]
age, name, *rest = data
print(data)
#Answer=[35.5, True].Extended sequence unpacking captures remaining unassigned elements into a standard list.


# Question 10
# What dictionary is produced by evaluating dict.fromkeys(["a", "b", "c"], 0)?
result = dict.fromkeys(["a", "b", "c"], 0)
print(result)
#Answer={"a": 0, "b": 0, "c": 0}.fromkeys() constructs a dictionary using sequence elements as keys, assigning the specified default value to each key.

