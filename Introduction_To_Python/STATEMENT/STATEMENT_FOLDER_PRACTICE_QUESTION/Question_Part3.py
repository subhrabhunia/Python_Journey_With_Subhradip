# Question 1
# What happens if the condition in an if statement evaluates to False?
# Answer=The block of code is skipped.When an if statement's condition is False, the interpreter bypasses the indented block of code underneath it.


# Question 2
# Which character must always appear at the end of an if, elif, or else line?
# Answer=colon (:).In Python, a colon is required to indicate the start of an indented block of code.


# Question 3
# What is the output of the following comparison: "20" == 20?
a="20"
b=20
print(a==b)
# Answer=False.Python strictly compares data types; a string containing a number is not equal to an integer of that number.


# Question 4
# In an if-elif-else chain, what happens if multiple conditions are True?
# Only the first matching block executes.Python evaluates conditions sequentially and skips the rest of the chain as soon as it finds the first True condition.


# Question 5
# What keyword is used to provide a default block of code if all preceding conditions are False?
# Answer=else.The else block catches any case that was not handled by the preceding if or elif conditions.


# Question 6
# What is the correct syntax for a conditional expression (ternary operator) in Python?
# Answer=value_if_true if condition else value_if_false.This represents the standard Python syntax for a one-line conditional expression.


# Question 7
# How do you check if a specific value exists inside a list like Numbers = [10, 20, 30]?
# Answer=if 20 in Numbers:(Your answer).The 'in' membership operator checks if the left operand exists within the sequence on the right.


# Question 8
# Which keyword acts similarly to a 'switch' statement in Python 3.10 and newer?
# Answer=match. The match keyword initiates structural pattern matching, which is Python's equivalent to switch statements.


# Question 9
# In a match statement, what signifies the default case if no other patterns match?
# Answer=case _:.The underscore (_) acts as a wildcard pattern that matches anything not caught by previous cases.


# Question 10
# How do you match multiple patterns in a single case statement (e.g., matching weekend days)?
# Answer=case 6 | 7:.The single pipe (|) acts as an OR operator within structural pattern matching.


# Question 11
# Consider age = 15. What is the result of Status = "Adult" if age >= 18 else "Minor"?
age=15
if age>=18:
    print("Adult")
else:
    print("Minor")
# Answer="Minor".Since 15 is not greater than or equal to 18, the ternary expression returns the value after 'else'.