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