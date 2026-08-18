#Question1
# What is the output of the addition operation 10 + 5?
a=10
b=5
result=a+b
print(result)
#Answer=The code uses the addition operator (+) to add the values of a and b together, outputting the final sum of 15.


#Question2
# Which operator calculates the remainder, and what is the specific result of 10 % 
c=10
d=5
print(c%d)
#Answer=The modulus operator (%) is used to calculate the remainder, and the specific result of 10 % 5 is 0.


# Question3
# How does the floor division operator (//) evaluate the expression 10 // 3?
e=10
f=3
print(e//f)
# Answer=The floor division operator (//) evaluates the expression by returning only the integer quotient, so the specific result of 10 // 3 is 3.


# Question4
# What is the output of the exponentiation calculation 2 ** 3?
m=2
n=3
print(m**n)
# Answer=The output of the exponentiation calculation 2 ** 3 is 8.  


# Question5
# If variables are set as g=10 and h=5, what is the exact float output of the division operation print(g/h)
g=10
h=5
print(g/h)
# Answer=The exact float output of the division operation print(g/h) is 2.0.


# Question6
# Does the expression 5 == 5 evaluate to True or False?
i=5
j=5
print(i==j)
# Answer=The == (Equal to) operator checks if two values are exactly the same. Since the number 5 is equal to itself, the condition is met and it outputs True.  


# Question7
# If you use the == operator to compare an integer and a string that hold the exact same value, what will the output be?
k="5"
l=5
print(k==l)
# Answer=Even if the values appear the same, comparing an integer and a string results in False because the == operator recognizes that they are different data types.


# Question8 
# Given the variables A=10 and B=20, what does the inequality check print(A!=B) output?  
A=10
B=20
print(A!=B)
# Answer=The != (Not equal to) operator checks if two variables are different from each other. Since 10 is not equal to 20, the condition is satisfied, resulting in True.  


# Questionn9 
# What does the >= operator specifically check for when comparing a first and second variable?
# Answer=It evaluates whether the first value is larger than the second value, or if the two variables are exactly the same. If either of these conditions is met, it outputs True.


# Question10
# If age=20, does the boolean condition age>=18 return True or False?
age=20
print(age>18)
# Answer=The >= operator checks if the value of age is greater than or equal to 18. Since 20 is strictly greater than 18, the condition is satisfied, resulting in True.


# Question 11
# In a logical and operation, what is the evaluated result of (5 > 2) and (10 > 5)?
print((5 > 2) and (10 > 5))
# Answer=The evaluated result is True[cite: 3]. The 'and' operator returns True if both conditions are True[cite: 3].


# Question 12
# If age=25 and salary=50000, what is the output of print(age>=18 and salary>=30000)?
age=25
salary=50000
print(age>=18 and salary>=30000)
# Answer=The output is True[cite: 3]. It checks if both conditions match; since both the age and salary conditions are met, it gives True[cite: 3].


# Question 13
# Under what specific condition will the logical or operator return a True result?
print((5 > 10) or (10 > 5))
# Answer=The logical 'or' operator returns True if at least one condition is True[cite: 3]. 


# Question 14
# If age1=15 and has_license=True, what is the final output of print(age1>=18 or has_license)?
age1=15
has_license=True
print(age1>=18 or has_license)
# Answer=The output is True[cite: 3]. If any one condition matches then it gives True; in this case, has_license is True[cite: 3].


# Question 15
# How does the not operator mathematically change the result of the expression not(5 > 2)?
print(not(5 > 2))
# Answer=The 'not' operator reverses the result, returning False if the evaluated result is True[cite: 3].


# Question 16
# What condition must be true for the is operator to return True when comparing two variables?
# Answer=Both variables must point to the same object[cite: 4].


# Question 17
# If x=[10,20,30] and y=[10,20,30], why does print(x is y) return False despite the lists containing the exact same values?
x=[10,20,30]
y=[10,20,30]
print(x is y)
# Answer=It returns False because the two variables store in different memory locations[cite: 4].


# Question 18
# Why does print(a is b) evaluate to True when the single value variables are set as a=100 and b=100?
a=100
b=100
print(a is b)
# Answer=It evaluates to True because single values store in the same memory location[cite: 4].


# Question 19
# What does the is not operator check for regarding the memory location of two objects?
# Answer=The 'is not' operator returns True if both variables point to different objects, meaning they store in different memory locations[cite: 4].


# Question 20
# Given c=[10,20,30] and d=c, what will the expression print(c is not d) output?
c=[10,20,30]
d=c
print(c is not d)
# Answer=The output is False because the two variables store in the same memory[cite: 4].


# Question 21
# What does the in operator return when checking the string condition "a" in "apple"?
print("a" in "apple")
# Answer=It returns True because the value exists in the sequence[cite: 5].


# Question 22
# If a list is defined as numbers=[20,30,10,40], what is the evaluated result of print(80 not in numbers)?
numbers=[20,30,10,40]
print(80 not in numbers)
# Answer=The evaluated result is True[cite: 5].


# Question 23
# In the dictionary student={"name":"John", "age":20}, why does print("John" in student) evaluate to False?
student={
    "name":"John",
    "age":20
}
print("John" in student)
# Answer=It evaluates to False because the 'in' operator checks the keys of the dictionary, not the values[cite: 5].


# Question 24
# If fruits = ["apple", "banana", "mango"], what does the condition print("orange" not in fruits) return?
fruits = ["apple", "banana", "mango"]
print("orange" not in fruits)
# Answer=The condition returns True[cite: 5].


# Question 25
# In the provided image extension script, what specific text prints if ".png" in filename evaluates to True?
filename="Photo.png"
if ".png" in filename:
    print("Image accepted")
# Answer=The specific text that prints is "Image accepted"[cite: 5].


# Question 26
# What is the final integer result of the bitwise AND expression 5 & 3?
print(5 & 3)
# Answer=The final integer result is 1[cite: 6].


# Question 27
# How does the bitwise XOR operator (^) set bits, and what is the output of 5 ^ 3?
print(5 ^ 3)
# Answer=The bitwise XOR operator sets a bit to 1 if the bits are different, and the output is 6[cite: 6].


# Question 28
# What is the mathematical expansion and final result of the left shift operation 5 << 3?
a=5
print(a<<3)
# Answer=The mathematical expansion is 5 x(2x2x2)[cite: 7]. This outputs a final result of 40.


# Question 29
# Based on the right shift operations formula, how is 20 >> 2 mathematically expanded?
b=20
print(b>>2)
# Answer=It is mathematically expanded as 20/(2x2)[cite: 7].


# Question 30
# According to the assignment operators table, what is the equivalent expression for x //= 3?
# Answer=The equivalent expression is x = x // 3[cite: 8].