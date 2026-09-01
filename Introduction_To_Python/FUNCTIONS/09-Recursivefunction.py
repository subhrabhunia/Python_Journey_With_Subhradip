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

def countdown(n):
    if n == 0:  # Base case to stop recursion
        print("Countdown complete!")
        return

    print(n)
    countdown(n-1)  # Recursive call with modified parameter
print("Countdown from 5:")
countdown(5)  # Start the countdown from 5

#factorial of a number using recursion of 5
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)  # Recursive call with modified parameter
print("Factorial of 5 is:", factorial(5))  # Output: Factorial of 5 is: 120