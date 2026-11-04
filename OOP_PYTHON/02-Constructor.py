# constructor function is a special type of function that is automatically called when an object of a class is created. It is used to initialize the attributes of the class. In Python, the constructor function is defined using the `__init__` method.

#1st example of constructor function in python:-
class Student:
    def __init__(self):  # The constructor function takes two parameters: name and age.
        self.name="Subhradip"  # The self parameter refers to the instance of the class. We use it to assign the values of name and age to the instance variables. self.age is a  property of the class Student. It is used to store the age of the student. The value of self.age is set to 22 in the constructor function.
        self.age=22
student=Student()
print(student.name)  # Output: Subhradip
print(student.age)  # Output: 22


#2nd program of constructor function in python:-
class Books:
    def __init__(self, title="Unknown", author="Unknown"):  # The constructor function takes two parameters: title and author.
        self.title = title  # The self parameter refers to the instance of the class. We use it to assign the values of title and author to the instance variables.
        self.author = author

    def display_info(self):  # This method displays the information about the book.
        print("Title:", self.title)
        print("Author:", self.author)
        print("--------------------")
books1=Books("Python Programming", "John Doe")  # Creating an object of the Books class and passing the title and author as arguments.
books2=Books("Java Programming")  # Creating another object of the Books class and passing the title and author as arguments.
books1.display_info()  # Calling the display_info method of the books1 object.
books2.display_info()  # Calling the display_info method of the books2 object.
print(type(books1))  # Output: <class '__main__.Books'> 

