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

