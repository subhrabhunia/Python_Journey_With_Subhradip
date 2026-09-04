# Built High order Functions: A higher-order function is a function that takes one or more functions as arguments and/or returns a function as its result. In Python, functions are first-class citizens, meaning they can be treated like any other object. This allows us to create higher-order functions that can operate on other functions.
# example:map(),filter(),reduce() are examples of high order functions.
# How to use map() function:
# The map() function applies a given function to all items in an iterable (like a list)
# map() function takes two arguments: a function and an iterable (like a list, tuple, etc.) and returns an iterator that applies the function to each item of the iterable.Function can be a built-in function or a user-defined function.External functions and Lambda functions can also be used with map() function.

#Example Squaring numbers in a list using map() function
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x*x
result = map(square, numbers)
print(list(result))  # Output: [1, 4, 9, 16, 25]

#Convert names in a list to uppercase using map() function
names = ['alice', 'bob', 'charlie']
results=map(str.upper,names)
print(list(results))  # Output: ['ALICE', 'BOB', 'CHARLIE']