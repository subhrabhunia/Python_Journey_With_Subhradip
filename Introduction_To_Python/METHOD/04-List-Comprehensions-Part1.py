# | Type           | Syntax                              | Result     |
# | -------------- | ----------------------------------- | ---------- |
# | **List**       | `[expression for item in iterable]` | List       |
# | **Set**        | `{expression for item in iterable}` | Set        |
# | **Dictionary** | `{key: value for item in iterable}` | Dictionary |
# | **Generator**  | `(expression for item in iterable)` | Generator  |
# List        → [ ]
# Set         → { }
# Dictionary  → {key : value}
# Generator   → ( )

#Advantages of comprehensions:-
# 1.Short and clean code
# 2.More readable than many loops
# 3.Often faster than manual for loops
# 4.Easy to combine filtering and transformation

# Avoid comprehensions when the logic becomes too complex,such as multiple nested conditions,several loops,or operations that are hard to read.

#Basic Example
numbers=[1,2,3,4,5]
squares=[num**2 for num in numbers]
print(squares)

#List convetator to Upper case
names=["amit","rahul","soumya"]
upper=[name.upper() for name in names]
print(upper)

#Find Length of list
length=[len(name) for name in names]
print(length)

#List Comprehensions with if statement
All_Numbers=[1,2,3,4,5,6,7,8]
Even_Numbers=[even for even in All_Numbers if even%2==0]
Odd_Numbers=[odd for odd in All_Numbers if odd%2!=0]
print(Even_Numbers)
print(Odd_Numbers)

#Extract Digits Filter
text="A1B2C3D4"
Digits=[ch for ch in text if ch.isdigit()]
print(Digits)

#Square of even numbers
Numbers=range(1,11)
Result=[Even**2 for Even in Numbers if Even%2==0]
print(Result)