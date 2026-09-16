# # PYTHON MODULES

# A module is a Python file (.py) that contains variables, functions,
# classes, and other Python code.

# Modules are used to organize code and reuse code in different programs.

# A Python file can be imported into another Python file as a module.

# ---

# 1. PYTHON MODULE

# ---

# A module is simply a Python file with a .py extension.

# Example:

# File1.py

# name = "Ram"

# def hello():
# print("hello world")

# class User:
# x = 5

# File1.py contains:

# * Variable -> name
# * Function -> hello()
# * Class -> User

# We can use these elements in another Python file by importing File1.

# ---

# 2. SELF-CREATED MODULE EXAMPLE

# ---

# File1.py

# name = "Ram"

# def hello():
# print("hello world")

# class User:
# x = 5

# File2.py

# import File1

# print(File1.name)
# File1.hello()

# Output:

# Ram
# hello world

# ---

# 3. TYPES OF PYTHON MODULES

# ---

# Python modules can mainly be divided into 3 types:

# 1. Python Files (Self-Created Modules)
# 2. Built-in Modules
# 3. Installed Packages (site-packages)

# ==================================================

# 1. PYTHON FILES (SELF-CREATED MODULE)
#    ==================================================

# These are Python files created by the programmer.

# They can contain:

# * Variables
# * Functions
# * Classes
# * Statements

# Example:

# File1.py

# name = "Ram"

# def hello():
# print("hello world")

# File2.py

# import File1

# print(File1.name)
# File1.hello()

# Output:

# Ram
# hello world

# Examples:

# * File1.py
# * calculator.py
# * student.py
# * quiz.py
# * timetable.py

# ==================================================
# 2) BUILT-IN MODULES
# ===================

# Built-in modules are modules that come with Python.

# They do not normally need to be installed separately.

# We can directly import and use them.

# Examples:

# import math
# import random
# import datetime
# import os
# import sys

# Example:

# import math

# print(math.sqrt(25))

# Output:

# 5.0

# Common Built-in Modules:

# math
# -> Used for mathematical operations

# random
# -> Used to generate random values

# datetime
# -> Used to work with date and time

# os
# -> Used for operating system related operations

# sys
# -> Used for Python system related operations

# ==================================================
# 3) INSTALLED PACKAGES (site-packages)
# =====================================

# Installed packages are external Python libraries/packages
# that are installed separately.

# They are commonly installed using pip.

# Example:

# pip install numpy

# After installation:

# import numpy

# Other examples:

# pip install pandas

# pip install requests

# pip install flask

# Examples of installed packages:

# NumPy
# -> Numerical and array operations

# Pandas
# -> Data analysis and data manipulation

# Requests
# -> Sending HTTP requests

# Flask
# -> Web application development

# Installed packages are generally stored in Python's
# site-packages directory.

# ==================================================
# IMPORTING MODULES
# =================

# There are several common ways to import modules in Python.

# ---

# 1. import module

# ---

# Syntax:

# import module_name

# Example:

# import File1

# print(File1.name)
# File1.hello()

# Here, the complete File1 module is imported.

# To access its elements, we use:

# module_name.element

# Example:

# File1.name
# File1.hello()

# ---

# 2. from module import function

# ---

# Syntax:

# from module_name import function_name

# Example:

# from File1 import hello

# hello()

# Here, only the hello function is imported from File1.

# We can call it directly without writing File1.

# ---

# 3. from module import *

# ---

# Syntax:

# from module_name import *

# Example:

# from File1 import *

# print(name)
# hello()

# It imports the available names from the module.

# It is generally better to explicitly import the names
# that are needed instead of using *.

# ---

# 4. import module as alias

# ---

# Syntax:

# import module_name as alias

# Example:

# import File1 as F

# print(F.name)
# F.hello()

# Here, F is an alias (short name) for File1.

# Instead of:

# File1.hello()

# we can write:

# F.hello()

# ==================================================
# DIFFERENCE BETWEEN IMPORT METHODS
# =================================

# 1. import File1

# Meaning:
# -> Import the complete module.

# Access:

# File1.name
# File1.hello()

# 2. from File1 import hello

# Meaning:
# -> Import only the hello function.

# Access:

# hello()

# 3. from File1 import *

# Meaning:
# -> Import available names from the module.

# Access:

# name
# hello()

# 4. import File1 as F

# Meaning:
# -> Import the module with an alias.

# Access:

# F.name
# F.hello()

# ==================================================
# COMPLETE EXAMPLE
# ================

# File1.py

# name = "Ram"

# def hello():
# print("hello world")

# class User:
# x = 5

# File2.py

# import File1
# from File1 import hello

# print(File1.name)
# File1.hello()
# hello()

# Output:

# Ram
# hello world
# hello world

# Explanation:

# import File1

# -> Imports the complete File1 module.

# print(File1.name)

# -> Accesses the name variable from File1.

# File1.hello()

# -> Calls the hello() function using the module name.

# from File1 import hello

# -> Imports the hello() function directly.

# hello()

# -> Calls the imported function directly.

# ==================================================
# MODULE vs PACKAGE
# =================

# MODULE:

# A module is usually a single Python file.

# Example:

# calculator.py

# PACKAGE:

# A package is a collection of Python modules organized
# in a directory.

# Example:

# mypackage/
# **init**.py
# calculator.py
# student.py
# teacher.py

# So:

# Module
# -> Usually one .py file

# Package
# -> Collection of modules in a directory

# ==================================================
# PIP
# ===

# PIP is a package management tool for Python.

# It is used to install external Python packages.

# Syntax:

# pip install package_name

# Examples:

# pip install numpy

# pip install pandas

# pip install requests

# To uninstall a package:

# pip uninstall package_name

# To see installed packages:

# pip list

# ==================================================
# SITE-PACKAGES
# =============

# site-packages is a directory where Python packages installed
# in the Python environment are generally stored.

# For example:

# Python
# |
# +-- Lib
# |
# +-- site-packages
# |
# +-- numpy
# +-- pandas
# +-- requests

# Packages installed using pip are generally placed in
# site-packages.

# ==================================================
# WHY USE MODULES?
# ================

# Modules are useful because they:

# 1. Reuse code
# 2. Organize code
# 3. Reduce code duplication
# 4. Make programs easier to maintain
# 5. Make large programs easier to manage
# 6. Allow functions and classes to be shared between files

# ==================================================
# QUICK REVISION
# ==============

# MODULE
# -> A Python file containing reusable code.

# 3 TYPES OF MODULES

# 1. Self-Created Module
#    -> Created by programmer
#    -> Example: File1.py

# 2. Built-in Module
#    -> Comes with Python
#    -> Example: math, random, os

# 3. Installed Package
#    -> Installed separately
#    -> Usually using pip
#    -> Example: numpy, pandas, requests

# IMPORT TYPES

# 1. import module

# 2. from module import function

# 3. from module import *

# 4. import module as alias

# EASY WAY TO REMEMBER

# Self-Created Module
# ↓
# Created by Us

# Built-in Module
# ↓
# Comes with Python

# Installed Package
# ↓
# Install using pip

# MODULE
# ↓
# Python File
# ↓
# Contains Variables + Functions + Classes
# ↓
# Can be Imported
# ↓
# Can be Reused


#Basic Example
import ModulesTest
ModulesTest.greeting("Subhradip")

print(ModulesTest.add(30,20))
print(ModulesTest.sub(30,20))

print(ModulesTest.test)

print(ModulesTest.Person['name'])
print(ModulesTest.Person['age'])
print(ModulesTest.Person['city'])

#alias
import ModulesTest as M
M.greeting("Subhradip")

print(M.add(30,20))
print(M.sub(30,20))

print(M.test)

print(M.Person['name'])
print(M.Person['age'])
print(M.Person['city'])

#from module
from ModulesTest import greeting
greeting("Soumya")

from ModulesTest import add
print(add(3,20))

from ModulesTest import sub,Person
print(sub(10,5))
print(Person['name'])

#Import Everything
from ModulesTest import*
print(add(30,20))
print(sub(30,20))
greeting("Subhradip")