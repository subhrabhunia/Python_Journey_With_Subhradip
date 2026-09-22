# # Python : Error & Exception Handling

# Python uses `try`, `except`, `else`, and `finally` to handle exceptions.

# ## Syntax

# ```python
# try:
#     # Your Code Goes Here

# except:
#     # When any error comes in try code

# else:
#     # Runs only if no exception occurs

# finally:
#     # Runs always, whether an exception occurs or not
# ```

# ## Example

# ```python
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number

# except:
#     print("An error occurred")

# else:
#     print("Result:", result)

# finally:
#     print("Program completed")
# ```

# ### If User Enters `2`

# ```text
# Enter a number: 2
# Result: 5.0
# Program completed
# ```

# ### If User Enters `0`

# ```text
# Enter a number: 0
# An error occurred
# Program completed
# ```

# ### Important Points

# * **`try`** → Contains the code that may cause an error.
# * **`except`** → Runs when an exception occurs.
# * **`else`** → Runs only when **no exception** occurs.
# * **`finally`** → Runs **always**, whether an exception occurs or not.


#else block example
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input")

else:
    print("You entered:", number)