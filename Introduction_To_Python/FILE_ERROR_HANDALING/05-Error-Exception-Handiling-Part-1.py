# # Python : Error Handling

# Errors are problems that occur while writing or executing a Python program.

# ## Types of Errors in Python

# There are mainly **3 types of errors**:

# ### 1. Syntax Error

# A **Syntax Error** occurs when the rules or syntax of Python are not followed correctly.

# ### Example:

# ```python
# if 5 > 2
#     print("Hello")
# ```

# ### Error:

# ```text
# SyntaxError
# ```

# The `:` is missing after `if 5 > 2`.

# ### Correct Code:

# ```python
# if 5 > 2:
#     print("Hello")
# ```

# ---

# ## 2. Runtime Error (Exception)

# A **Runtime Error** occurs while the program is running.

# These errors are also called **Exceptions**.

# ### Example:

# ```python
# print(5 / 0)
# ```

# ### Error:

# ```text
# ZeroDivisionError
# ```

# A number cannot be divided by zero.

# ---

# ## 3. Logical Error

# A **Logical Error** occurs when the program runs successfully but produces the **wrong output** because the logic is incorrect.

# ### Example:

# ```python
# length = 10
# width = 5

# area = length + width

# print(area)
# ```

# ### Output:

# ```text
# 15
# ```

# But the correct formula for the area of a rectangle is:

# ```text
# Area = length × width
# ```

# ### Correct Code:

# ```python
# length = 10
# width = 5

# area = length * width

# print(area)
# ```

# ### Output:

# ```text
# 50
# ```

# ---

# # Python Error Handling

# Python provides **Exception Handling** to handle runtime errors without stopping the entire program unexpectedly.

# The main keywords are:

# * `try`
# * `except`
# * `else`
# * `finally`

# ## try

# The `try` block contains the code that may produce an error.

# ### Syntax:

# ```python
# try:
#     # Your Code Goes Here
# ```

# ## except

# The `except` block runs when an error occurs in the `try` block.

# ### Syntax:

# ```python
# except:
#     # When any error comes in try code
# ```

# ## Basic Structure

# ```python
# try:
#     # Your Code Goes Here

# except:
#     # When any error comes in try code
# ```

# ### Example:

# ```python
# try:
#     print(5 / 0)

# except:
#     print("An error occurred")
# ```

# ### Output:

# ```text
# An error occurred
# ```

# Instead of stopping the program with an unhandled exception, Python executes the `except` block.


# Python : Common Built-in Exceptions

# Python provides many **built-in exceptions** to handle different types of runtime errors.

# ## 1. ZeroDivisionError

# Occurs when a number is divided by zero.

# ```python
# print(10 / 0)
# ```

# ---

# ## 2. ValueError

# Occurs when a function receives a value of the correct type but an invalid value.

# ```python
# age = int("abc")
# ```

# ---

# ## 3. TypeError

# Occurs when an operation or function is used with an inappropriate data type.

# ```python
# print("10" + 5)
# ```

# ---

# ## 4. NameError

# Occurs when a variable or name is used before it is defined.

# ```python
# print(name)
# ```

# ---

# ## 5. IndexError

# Occurs when trying to access an index that does not exist in a list, tuple, or similar sequence.

# ```python
# numbers = [10, 20, 30]

# print(numbers[5])
# ```

# ---

# ## 6. KeyError

# Occurs when trying to access a dictionary key that does not exist.

# ```python
# student = {"name": "Rahul"}

# print(student["age"])
# ```

# ---

# ## 7. AttributeError

# Occurs when an object does not have the specified attribute or method.

# ```python
# name = "Python"

# name.append("Hello")
# ```

# ---

# ## 8. FileNotFoundError

# Occurs when trying to open a file that does not exist.

# ```python
# file = open("abc.txt", "r")
# ```

# ---

# ## 9. PermissionError

# Occurs when an operation does not have the required permission.

# ```python
# # Example: trying to access a file without sufficient permission
# ```

# ---

# ## 10. ImportError

# Occurs when a requested name cannot be imported from a module.

# ```python
# from math import abc
# ```

# ---

# ## 11. ModuleNotFoundError

# Occurs when Python cannot find the specified module.

# ```python
# import xyz
# ```

# ---

# ## 12. RuntimeError

# Occurs when an error happens during program execution that does not fit another specific exception type.

# ```python
# raise RuntimeError("Something went wrong")
# ```

# ---

# ## 13. AssertionError

# Occurs when an `assert` statement fails.

# ```python
# age = 15

# assert age >= 18
# ```

# ---

# ## 14. MemoryError

# Occurs when a program cannot allocate enough memory.

# ```python
# # Example: trying to create an extremely large object
# ```

# ---

# ## 15. RecursionError

# Occurs when the maximum recursion depth is exceeded.

# ```python
# def test():
#     test()

# test()
# ```

# ---

# ## 16. TimeoutError

# Occurs when a system operation or function takes longer than the allowed time.

# ```python
# # Example: an operation exceeds its timeout limit
# ```

# ---

# ## 17. NotImplementedError

# Used when a method or feature is intentionally not implemented.

# ```python
# def calculate():
#     raise NotImplementedError
# ```

# ---

# ## 18. UnicodeEncodeError

# Occurs when a Unicode string cannot be encoded using a particular encoding.

# ```python
# # Example: a character cannot be encoded using the selected encoding
# ```

# ---

# ## 19. UnicodeDecodeError

# Occurs when bytes cannot be decoded using a particular encoding.

# ```python
# # Example: invalid bytes cannot be decoded using UTF-8
# ```

# # Quick Revision Table

# | Exception             | Meaning                        |
# | --------------------- | ------------------------------ |
# | `ZeroDivisionError`   | Division by zero               |
# | `ValueError`          | Invalid value                  |
# | `TypeError`           | Wrong/inappropriate data type  |
# | `NameError`           | Name or variable not defined   |
# | `IndexError`          | Invalid sequence index         |
# | `KeyError`            | Dictionary key not found       |
# | `AttributeError`      | Attribute or method not found  |
# | `FileNotFoundError`   | File does not exist            |
# | `PermissionError`     | Permission denied              |
# | `ImportError`         | Import cannot be performed     |
# | `ModuleNotFoundError` | Module cannot be found         |
# | `RuntimeError`        | General runtime error          |
# | `AssertionError`      | Assertion failed               |
# | `MemoryError`         | Insufficient memory            |
# | `RecursionError`      | Recursion limit exceeded       |
# | `TimeoutError`        | Operation timed out            |
# | `NotImplementedError` | Feature/method not implemented |
# | `UnicodeEncodeError`  | Unicode encoding failed        |
# | `UnicodeDecodeError`  | Unicode decoding failed        |
