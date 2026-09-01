# A function that calls itself untill a stopping condition is reached .
# SYNTAX:-
# def recursive_function(parameter):
#     if base_case:
#         return value 
#     code statement
#     return recursive_function(modified_parameter)

def print_numbers(n):
    if n > 5:  # Base case to stop recursion
        return

    print(n)
    print_numbers(n+1)  # Recursive call with modified parameter
print_numbers(1)  # Start the recursion with initial value 1