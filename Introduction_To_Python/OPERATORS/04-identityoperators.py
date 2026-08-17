# | Operator | Description                                                  | Example      | Result            |
# | -------- | ------------------------------------------------------------ | ------------ | ----------------- |
# | `is`     | Returns `True` if both variables point to the same object.   | `a is b`     | `True` or `False` |
# | `is not` | Returns `True` if both variables point to different objects. | `a is not b` | `True` or `False` |


x=[10,20,30]
z=x
y=[10,20,30]

print(x is y)  #Its print false because its two values are same but two varriables store in different different memory locations.It is for list dictionar set tuple.
print(x is z)

a=100
b=100
print(a is b)  #if two varriables has single values then its stores same memory location so its give true.


c=[10,20,30]
d=c  
e=[10,20,30]
print(c is not e) #Its print True because two varriables stores diferent memory.
print (c is not d) #Its print False beacuse two varriables store in same memory.
