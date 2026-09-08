# SYNTAX:
# def function_name:
#         yield"FIRST"   ------>yield means Pause
#         yield"SECOND"
#         yield"THIRD"
# g=function_name()
# print(next(g))----->print FIRST
# print(next(g))----->print SECOND
# print(next(g))----->print THIRD

#Basic Example
def numbers():
    yield 1
    yield 2
    yield 3
g=numbers()
print(next(g))
print(next(g))
print(next(g))

#Example with string 
def string_value():
    yield "Soumya"
    yield "Ram"
    yield "Shayam"
generator=string_value()
print(next(generator))
print("*****************")
print("*****************")
print(next(generator))
print("*****************")
print("*****************")
print("*****************")
print(next(generator))

#Don't print first two value print last value
def fruits():
    yield "Apple"
    yield "Banana"
    yield "Grapes"
generators=fruits()
next(generators)
print("*****************")
print("*****************")
next(generators)
print("*****************")
print("*****************")
print("*****************")
print(next(generators))

#Generator in  for loop
def games():
    yield "Cricket"
    yield "Football"
    yield "Hocky"
for i in games():
    print(i)