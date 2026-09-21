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


# # Python : try-except

# The `try-except` statement is used to **handle errors (exceptions)** in Python.

# ## Basic Example

# ```python
# try:
#     print(10 / 0)

# except:
#     print("An error occurred")
# ```

# ### Output

# ```text
# An error occurred
# ```

# ## Example with Specific Exception

# ```python
# try:
#     number = int(input("Enter a number: "))
#     print(10 / number)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("Please enter a valid number")
# ```

# ### Example Output 1

# If the user enters:

# ```text
# 0
# ```

# Output:

# ```text
# Cannot divide by zero
# ```

# ### Example Output 2

# If the user enters:

# ```text
# abc
# ```

# Output:

# ```text
# Please enter a valid number
# ```

# ### Example Output 3

# If the user enters:

# ```text
# 2
# ```

# Output:

# ```text
# 5.0
# ```

# ## Syntax

# ```python
# try:
#     # Code that may cause an error

# except:
#     # Code executed when an error occurs
# ```

# ### Important

# * `try` → Contains code that may cause an exception.
# * `except` → Handles the exception.
# * Using a **specific exception** such as `ZeroDivisionError` or `ValueError` is generally better than using a bare `except`.

try:
    a = 10
    b = 0

    print(a / b)

except:
    print("Cannot divide by zero")

try:
    number = int(input("Enter a number: "))
    print(number)

except:
    print("Please enter a valid number")

# Catching a Specific Exception

# In Python, we can catch a **specific exception** by writing the exception name after the `except` keyword.

# This allows us to handle different errors in different ways.

# ## Syntax

# ```python
# try:
#     # Code that may cause an error

# except ExceptionName:
#     # Code to handle the specific exception
# ```

# ## Example

# ```python
# try:
#     number = int(input("Enter a number: "))

#     result = 10 / number

#     print(result)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("Please enter a valid number")
# ```

# ### Output 1

# If the user enters:

# ```text
# 0
# ```

# Output:

# ```text
# Cannot divide by zero
# ```

# ### Output 2

# If the user enters:

# ```text
# abc
# ```

# Output:

# ```text
# Please enter a valid number
# ```

# ### Output 3

# If the user enters:

# ```text
# 2
# ```

# Output:

# ```text
# 5.0
# ```

# ## Important

# * `ZeroDivisionError` → Handles division by zero.
# * `ValueError` → Handles invalid values.
# * Multiple `except` blocks can be used for different exceptions.
# * Catching specific exceptions makes the program easier to understand and debug.
try:
    number = int(input("Enter a number: "))

    print(10 / number)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

# Python : Exception Object (`as` Keyword)

# The `as` keyword is used with `except` to store the **exception object** in a variable.

# This allows us to access the **error message/details** of the exception.

# ## Syntax

# ```python
# try:
#     # Code that may cause an error

# except Exception as e:
#     print(e)
# ```

# Here:

# * `Exception` → Type of exception.
# * `as e` → Stores the exception object in variable `e`.
# * `e` → Can be used to display the error message.

# ## Example

# ```python
# try:
#     print(10 / 0)

# except ZeroDivisionError as e:
#     print("Error:", e)
# ```

# ### Output

# ```text
# Error: division by zero
# ```

# ## Another Example

# ```python
# try:
#     number = int("abc")

# except ValueError as e:
#     print("Error:", e)
# ```

# ### Output

# ```text
# Error: invalid literal for int() with base 10: 'abc'
# ```

# ## Important Note

# ```python
# except ZeroDivisionError as e:
# ```

# Here `e` contains the **exception object**, which provides information about what went wrong.

# ### Short Form

# ```python
# try:
#     print(10 / 0)

# except Exception as e:
#     print(e)
# ```

# **`as` → Used to give a variable name to the exception object.**

try:
    print(10 / 0)

except ZeroDivisionError as e:
    print("Error:", e)