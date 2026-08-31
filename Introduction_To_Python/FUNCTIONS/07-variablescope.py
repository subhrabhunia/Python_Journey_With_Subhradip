# | Scope         | Where variable is created | Where it can be accessed                          | Example                       |
# | ------------- | ------------------------- | ------------------------------------------------- | ----------------------------- |
# | **Local**     | Inside a function         | Only inside that function                         | `x = 10` inside `demo()`      |
# | **Enclosing** | Inside an outer function  | Inside the outer function and its inner functions | `x = 10` inside `outer()`     |
# | **Global**    | Outside all functions     | Throughout the program                            | `x = 100`                     |
# | **Built-in**  | Provided by Python        | Anywhere                                          | `print()`, `len()`, `input()` |
# x = "Global"

# def outer():
#     y = "Enclosing"

#     def inner():
#         z = "Local"

#         print(z)
#         print(y)
#         print(x)
#         print(len("Python"))

#     inner()

# outer()