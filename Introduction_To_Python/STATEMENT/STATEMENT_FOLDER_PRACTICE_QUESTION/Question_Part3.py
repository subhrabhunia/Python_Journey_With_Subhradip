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


# Question 12
# What is the primary purpose of a nested if statement?
# Answer=To check a condition only if a previous condition is true.Nesting places one conditional inside the block of another, executing only when the outer block's condition is met.


# Question 13
# In the dictionary match case {"Name": Name, "Age": Age}:, what happens to the variables Name and Age?
# Answer=They are bound to the values found in the dictionary.Pattern matching allows you to unpack data structures and bind their internal elements to new variables.


# Question 14
# What is a 'guard' in a Python match statement?
# Answer=An if condition attached to a case.A guard provides an additional boolean check that must evaluate to True for the case to succeed.


# Question 15
# What happens if a match statement doesn't have a case _: and no patterns match the input?
# Answer=Execution silently continues to the next block of code.
# If no cases match and there is no default wildcard case, the statement acts like a missed if-block and just moves on.


# Question 16
# Evaluate this statement: Result = "Even" if number % 2 else "Odd". What does number % 2 evaluate to when number is 4?
# Answer=False.4 divided by 2 leaves a remainder of 0. Because 0 is 'falsy', the ternary takes the else path.


# Question 17
# In the expression if (User_Name == "Admin" and Password == 1234):, what does and signify?
# Answer=Both conditions must be True.The logical 'and' operator strictly requires all operands to evaluate to True for the whole expression to be True.


# Question 18
# If you want to match a tuple but only care about the second value being 20, which pattern is correct?
# Answer=case (_, 20):.The underscore acts as a wildcard placeholder for exactly one element you want to ignore.


# Question 19
# What does the code list = [10, 20]; match list: case [10]: print("Found") output?
# Answer=It prints nothing.The pattern [10] does not structurally match [10, 20], and with no default case, execution continues silently.


# Question 20
# When defining an if block, how does Python know which lines of code belong inside the block?
# Answer=By the level of indentation.Python strictly enforces indentation (spaces or tabs) to define structural blocks of code.


# Question 21
# In Python's match statement, do cases 'fall through' to the next case automatically?
# Answer=No, it executes the block and then exits.Python executes only the first matching case and immediately exits the match block without needing a break.


# Question 22
# What is the result of applying float() to the string input() in float(input("Enter Your Age:"))?
# Answer=It converts the string input into a floating-point number.Because input() always returns a string, wrapping it in float() explicitly casts that string into a decimal number for mathematical comparison.


# Question 23
# Which of the following describes chaining multiple conditions in a single ternary expression?
# Answer="A" if marks >= 90 else "B" if marks >= 60 else "C".This syntax effectively mimics an if-elif-else chain within a single line using nested ternary operators.


# Question 24
# What is the difference between sequential if statements and an if-elif chain?
# Answer=If-elif ensures only one block executes; sequential ifs evaluate independently.An if-elif chain stops checking once it finds a True condition, guaranteeing a single path. Sequential ifs check every condition regardless.


# Question 25
# Consider case (0, y):. What kind of structural match is this performing?
# Answer=Matching a tuple where the first element is exactly 0.The parentheses indicate a tuple. The 0 is a literal check, and y binds to whatever the second element is.


# Question 26
# Why is != used in the conditional if user_Name != "Admin":?
# Answer=To check if the two values are not equal.The bang-equals (!=) is the standard Python comparison operator for 'not equal to'.


# Question 27
# What is wrong with the code if a = 10: print("Matched")?
# Answer=It uses an assignment operator instead of equality.A single '=' attempts to assign 10 to 'a', causing a SyntaxError. Conditional checks require '=='.


# Question 28
# When matching case x if x <= 13:, what is x?
# Answer=A variable binding the matched value.Because 'x' is just a variable name, it catches the input value, and then the guard condition evaluates it.\


# Question 29
# Can you use logical operators like and or or outside of if statements?
# Answer=Yes, they can evaluate boolean logic anywhere.You can assign the result of logical operators directly to variables or use them in while loops and print statements.


# Question 30
# What is the primary benefit of structural pattern matching over complex if-elif chains?
# Answer=It improves readability and allows unpacking data structures.Match-case makes complex checks cleaner and can extract variables directly from lists, tuples, and dictionaries.