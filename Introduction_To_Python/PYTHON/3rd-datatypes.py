"""Different data types in python"""
# x="Hello World!" #This is String value.A variable named x is created and assigned the string value "Hello World!". In Python, variables are used to store data values, and they can be assigned using the equal sign (=). The variable name can be any valid identifier, and it is case-sensitive.
# x=20 #This is Numeric value.A variable named x is created and assigned the integer value 20. In Python, variables can hold different data types, including integers, strings, floats, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=20.5 #This is Float value.A variable named x is created and assigned the float value 20.5. In Python, variables can hold different data types, including integers, strings, floats, and more. The variable name can be any valid identifier, and it is case-sensitive. 
# x=True #This is Boolean value.A variable named x is created and assigned the boolean value True. In Python, variables can hold different data types, including integers, strings, floats, booleans, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=["apple","banana","cherry"] #This is List value.A variable named x is created and assigned the list value ["apple","banana","cherry"]. In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=("apple","banana","cherry") #This is Tuple value.A variable named x is created and assigned the tuple value ("apple","banana","cherry"). In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x={"name":"John","age":30} #This is Dictionary value.A variable named x is created and assigned the dictionary value {"name":"John","age":30}. In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x={20,30,40} #This is Set value.A variable named x is created and assigned the set value {20,30,40}. In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, sets, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=4+3j #This is Complex value.A variable named x is created and assigned the complex value 4+3j. In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, sets, complex numbers, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=range(6) #This is Range value.A variable named x is created and assigned the range value range(6). In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, sets, complex numbers, ranges, and more. The variable name can be any valid identifier, and it is case-sensitive.  
# x=frozenset({1, 2, 3}) #This is Frozen Set value.A variable named x is created and assigned the frozenset value frozenset({1, 2, 3}). In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, sets, complex numbers, ranges, frozensets, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=None #This is None value.A variable named x is created and assigned the None value None. In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, sets, complex numbers, ranges, frozensets, NoneType, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=b"Hello World!" #This is Bytes value.A variable named x is created and assigned the bytes value b"Hello World!". In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, sets, complex numbers, ranges, frozensets, NoneType, bytes, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=bytearray(5) #This is Bytearray value.A variable named x is created and assigned the bytearray value bytearray(5). In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, sets, complex numbers, ranges, frozensets, NoneType, bytes, bytearrays, and more. The variable name can be any valid identifier, and it is case-sensitive.
# x=memoryview(bytes(5)) #This is Memoryview value.A variable named x is created and assigned the memoryview value memoryview(bytes(5)). In Python, variables can hold different data types, including integers, strings, floats, booleans, lists, tuples, dictionaries, sets, complex numbers, ranges, frozensets, NoneType, bytes, bytearrays, memoryviews, and more. The variable name can be any valid identifier, and it is case-sensitive.


x="HelloWorld!"
print(type(x)) #The above line prints the data type of the variable x, which is <class 'str'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable x holds a string value, so the output will indicate that it is of type 'str'.

y=25
print(type(y)) #The above line prints the data type of the variable y, which is <class 'int'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable y holds an integer value, so the output will indicate that it is of type 'int'.

z=30.30
print(type(z)) #The above line prints the data type of the variable z, which is <class 'float'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable z holds a float value, so the output will indicate that it is of type 'float'.

a=3+4
print(type(a)) #The above line prints the data type of the variable a, which is <class 'int'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable a holds an integer value, so the output will indicate that it is of type 'int'.   

b=4+4.4
print(type(b)) #The above line prints the data type of the variable b, which is <class 'float'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable b holds a float value, so the output will indicate that it is of type 'float'.  

c=4+3j 
print(type(c)) #The above line prints the data type of the variable c, which is <class 'complex'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable c holds a complex number value, so the output will indicate that it is of type 'complex'. 

d=True
print(type(d)) #The above line prints the data type of the variable d, which is <class 'bool'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable d holds a boolean value, so the output will indicate that it is of type 'bool'.

e="True"
print(type(e)) #The above line prints the data type of the variable e, which is <class 'str'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable e holds a string value, so the output will indicate that it is of type 'str'.

f= 5>4
print(f) #The above line prints the value of the variable f, which is True. The expression 5>4 evaluates to True, and the result is assigned to the variable f. When we print the variable f, it displays the boolean value True.   
print(type(f)) #The above line prints the data type of the variable f, which is <class 'bool'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable f holds a boolean value, so the output will indicate that it is of type 'bool'.  

g= 5<4
print(g) #The above line prints the value of the variable g, which is False.            
print(type(g)) #The above line prints the data type of the variable g, which is <class 'bool'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable g holds a boolean value, so the output will indicate that it is of type 'bool'.  

h= 5==4
print(h) #The above line prints the value of the variable h, which is False.            
print(type(h)) #The above line prints the data type of the variable h, which is <class 'bool'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable h holds a boolean value, so the output will indicate that it is of type 'bool'.

i=["apple","banana","cherry"]
print(i)
print(type(i)) #The above line prints the data type of the variable i, which is <class 'list'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable i holds a list value, so the output will indicate that it is of type 'list'.

j=("apple","banana","cherry")
print(j)    
print(type(j)) #The above line prints the data type of the variable j, which is <class 'tuple'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable j holds a tuple value, so the output will indicate that it is of type 'tuple'.  

k=range(6)
print(k)
print(type(k)) 
print(list(k)) #The above line prints the data type of the variable k, which is <class 'range'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable k holds a range value, so the output will indicate that it is of type 'range'. The list() function is used to convert the range object into a list, and it prints the list representation of the range, which is [0, 1, 2, 3, 4, 5].    

m={"name":"John","age":30,"city":"New York","course":"Python"}
print(m)
print(type(m)) #The above line prints the data type of the variable m, which is <class 'dict'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable m holds a dictionary value, so the output will indicate that it is of type 'dict'.   

n={20,30,40,50}
print(n)
print(type(n)) #The above line prints the data type of the variable n, which is <class 'set'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable n holds a set value, so the output will indicate that it is of type 'set'.    

o=frozenset([1,2,3,4,5])
print(o)
print(type(o)) #The above line prints the data type of the variable o, which is <class 'frozenset'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable o holds a frozenset value, so the output will indicate that it is of type 'frozenset'.      

q=None
print(q)
print(type(q)) #The above line prints the data type of the variable q, which is

r=b"Hello World!"
print(r)
print(type(r)) #The above line prints the data type of the variable r, which is <class 'bytes'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable r holds a bytes value, so the output will indicate that it is of type 'bytes'.  

s=bytearray([5,6,7,8,9])
print(s)
print(type(s)) #The above line prints the data type of the variable s, which is <class 'bytearray'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable s holds a bytearray value, so the output will indicate that it is of type 'bytearray'.  

t=memoryview(bytes([45,46,47,48,49]))
print(t)
print(type(t)) #The above line prints the data type of the variable t, which is <class 'memoryview'>. The type() function is used to determine the data type of a variable in Python. In this case, the variable t holds a memoryview value, so the output will indicate that it is of type 'memoryview'.   
