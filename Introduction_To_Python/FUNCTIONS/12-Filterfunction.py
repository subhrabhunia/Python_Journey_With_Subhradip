# SYNTAX:-
# The filter() function returns only the elements that satisfy a certain condition from an iterable (like a list, tuple, etc.). It takes two arguments: a function and an iterable. The function should return either True or False for each element in the iterable. The filter() function returns an iterator that contains only the elements for which the function returned True.
# filter(function, iterable)

# | Feature                       | `map()` Function                  | `filter()` Function              |
# | ----------------------------- | --------------------------------- | -------------------------------- |
# | **Purpose**                   | Modifies/transforms every element | Selects some elements            |
# | **Returns**                   | Transformed values                | Matching values                  |
# | **Function should return**    | Any value                         | `True` or `False`                |
# | **Number of output elements** | Same as input                     | Same or fewer than input         |
# | **Common use cases**          | Convert, calculate, format        | Search, validate, remove, filter |

#Basic Example of filter() function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(num):
    return num % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]

#Not even numbers using filter() function
def is_not_even(num):
    return num % 2 != 0
odd_numbers = filter(is_not_even, numbers)
print(list(odd_numbers))  # Output: [1, 3, 5, 7, 9]

#Adult ages using filter() function
ages = [12, 17, 19, 24, 30, 15, 18]
results = filter(lambda age: age >= 18, ages)
print(list(results))  # Output: [19, 24, 30, 18]


#String Example
word=["Cat","Dog","Elephant","Lion","Tiger"]
results = filter(lambda x: len(x) > 3, word)
print(list(results))  # Output: ['Elephant', 'Lion', 'Tiger']  


#Real Example of filter() function
# Suppose we have a list of dictionaries representing people, and we want to filter out only the adults (age 18 and above) from that list.
email=[
    "subhradip9971@gmail.com",
    "rahul",
    "soumya@gmail.com",
    "hello"
]
answer=filter(lambda x: "@" in x, email)
print(list(answer))  # Output: ['subhradip9971@gmail.com', 'soumya@gmail.com']

#Employee eligable for bonus using filter() function
salaries = [25000, 30000, 40000, 50000, 60000]
eligible_for_bonus = filter(lambda salary: salary >= 40000, salaries)
bonus=map(lambda salary: salary +5000, eligible_for_bonus)
print(list(bonus))  # Output: [45000, 55000, 65000]