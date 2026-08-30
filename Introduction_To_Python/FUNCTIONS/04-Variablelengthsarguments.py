# def sum(*args):
#     Code Statement.  *Star meanslength arguments and args or any other name work as Tuple.Accept any  number of positional arguments. in star argument we set multiple value.

#example
def num (*args):
    print(args)

num(10)
num(10,20)
num(10,20,30)

#print with index number
def numbers(*test):    
    print(test[0])
    print(test[2])   

numbers(10,20,30)

#print with loop
def number(*tests):    
    for numb in tests:
        print(numb)
number(10,20,30)

#Sum of all numbers
def total(*all_numbers):
    result=0
    for numbe in all_numbers:
        result+=numbe
    return result

print(total(10,20,30))
print(total(40,50,60))
print(total(70,80,90))


#String argument
def student(*names):
    print("Student list:")

    for name in names:
        print(name)

student("Rahul", "Riya", "Amit", "Ankita")

#pass normal argument
def students(message,*name):
    print("Students list:")

    for nam in name:
        print(nam)

student("Hello","Rahul", "Riya", "Amit", "Ankita")