# 1. What is a Class?
# A Class is a blueprint or template used to create objects. It defines the properties (data) and methods (functions) that an object will have.
#Example:-A Car class defines properties such as color, brand, and speed, along with methods such as start(), stop(), and drive().

#2.What is an Object?
# An Object is an instance of a class. It represents a real-world entity and uses the properties and methods defined in the class.
#Example:-BMW, Audi, and Toyota are objects of the Car class.

# 3.Difference Between Class and Object in OOP
# | Class                                                                          | Object                                             |
# | ------------------------------------------------------------------------------ | -------------------------------------------------- |
# | 1. A class is a blueprint or template.                                         | 1. An object is an instance of a class.            |
# | 2. A class is a logical entity.                                                | 2. An object is a physical entity.                 |
# | 3. A class defines properties and methods.                                     | 3. An object uses properties and methods.          |
# | 4. A class is declared using the `class` keyword.                              | 4. An object is created using the class name.      |
# | 5. A class is declared once.                                                   | 5. Multiple objects can be created from one class. |
# | 6. A class does not occupy memory for instance data until objects are created. | 6. An object occupies memory when it is created.   |
# | 7. Example: Student.                                                           | 7. Example: s1, s2.                                |

# 4.What is Properties & Methods ?
#a.Properties (Attributes)
# Properties are the variables or characteristics of a class that store information about an object.
# Example: Name, age, roll number, colour, etc.

#b.Methods
# Methods are functions defined inside a class that describe the behaviour or actions of an object.
# Example: display(), eat(), run(), study(), etc.

#Class and object syntax:-
# class hello:
#     def message(self):  --->Methods are defined inside the class using the def keyword. The self parameter refers to the instance of the class.
#       console.log("Hello World")
# a= hello() ---> a is object of class hello. The object is created by calling the class name followed by parentheses.
# a.message() 

#Inbuilt class in python:-
x= 10
name= "Subhradip"
numbers=[1,2,3,4,5]
print(type(x))  # <class 'int'>
print(type(name))  # <class 'str'>
print(type(numbers))  # <class 'list'>

#First class and object example in python:-
class hello:
    test="----Test----"  # This is a class variable. It is shared among all instances of the class.
    def message(self,Name):
        print("Hello",Name)
        print(self.test)  # Accessing the class variable using self.

    def bye(self,Names):
        print("Goodbye",Names)
a= hello()  # a is object of class hello. The object is created by calling the class name followed by parentheses.
a.message("Subhradip")  # Calling the message method of the hello class using the object a.
#a.bye()  # Calling the bye method of the hello class using the object a.

b=hello()  # b is another object of class hello. The object is created by calling the class name followed by parentheses.
b.bye("Python")  # Calling the message method of the hello class using the object b.