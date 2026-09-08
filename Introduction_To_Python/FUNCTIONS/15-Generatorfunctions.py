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