# In logical operators check many condition in same time.Using many comparison creates a logical operators.

# | Operator | Description                                                   | Example                | Result  |
# | -------- | ------------------------------------------------------------- | ---------------------- | ------- |
# | `and`    | Returns `True` if both conditions are `True`.                 | `(5 > 2) and (10 > 5)` | `True`  |
# | `or`     | Returns `True` if at least one condition is `True`.           | `(5 > 10) or (10 > 5)` | `True`  |
# | `not`    | Reverses the result. Returns `False` if the result is `True`. | `not(5 > 2)`           | `False` |

age=25
salary=50000
print(age>=18 and salary>=30000)  #Its check two codition is match or not if two conditions match then give True ifany one condition not match then give False.

age1=15
has_license=True
print(age1>=18 or has_license)  #If sny one condition match then Give True if two comndition not match then give False.
print(age1>=18 or has_license==False) 

age2=20
print(not(age2>18))  #Reverse the result.