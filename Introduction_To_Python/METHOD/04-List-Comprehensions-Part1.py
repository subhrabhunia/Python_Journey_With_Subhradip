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
