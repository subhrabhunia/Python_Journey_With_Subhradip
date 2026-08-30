#def demo(**args):
#    code statement.    Its works as a dictionary.its accept any number of keyword arguments.** means keyword arguments

# Basic example
def student(**keywordargs):
    print(keywordargs)
student(name="Subhraip",age=20,city="Kolkata")

#if print one by boone value
def students(**keyarg):
    print(keyarg['name'])     
    print(keyarg['age'])
    print(keyarg['city'])
students(name="Subhraip",age=20,city="Kolkata")


#using loop
def students_Name(**keyargs):
    for key, value in keyargs.items():
        print(key, ":", value)
students_Name(name="Subhraip", age=20, city="Kolkata")

# Positional Argument

def display(*args, **kwargs):
    print("Positional Argument:")

    for value in args:
        print(value)

    print()

    print("Keyword Argument:")

    for key, value in kwargs.items():
        print(key, ":", value)


display(
    10,
    20,
    30,
    name="Soumya",
    age=20,
    city="Kolkata"
)
#Normal arguments
def demo(name, age, *skill, **details):
    print("Name:", name)
    print("Age:", age)

    print("Skills:")
    for s in skill:
        print(s)

    print("Details:")
    for key, value in details.items():
        print(key, ":", value)


demo(
    "Soumya",
    20,
    "Python",
    "HTML",
    "CSS",
    city="Kolkata",
    college="Adamas University"
)