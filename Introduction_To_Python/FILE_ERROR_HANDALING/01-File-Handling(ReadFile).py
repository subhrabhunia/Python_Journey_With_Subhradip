# # Python : Files

# A **File** is a collection of data stored permanently on a computer.

# ## Types of Files

# There are mainly two types of files:

# 1. Text Files
# 2. Binary Files

# ## 1. Text Files

# Text Files are **human-readable files**.

# They store data in the form of characters and text.

# ### Examples:

# * `.txt` → Text File
# * `.csv` → Comma Separated Values File
# * `.json` → JSON File
# * `.html` → HTML File
# * `.css` → CSS File
# * `.py` → Python File
# * `.xml` → XML File

# ### Example:

# students = ["Rahul", "Amit", "Neha"]

# Text files can be opened and read using a normal text editor.

# ### Features:

# * Human-readable
# * Stores text and characters
# * Easy to create and edit
# * Can be opened using a text editor

# ## 2. Binary Files

# Binary Files are **not directly human-readable**.

# They store data in the form of **binary/bytes**.

# ### Examples:

# * `.jpg` → Image File
# * `.png` → Image File
# * `.mp3` → Audio File
# * `.mp4` → Video File
# * `.exe` → Executable File
# * `.pdf` → PDF File

# ### Features:

# * Not directly human-readable
# * Stores data as bytes
# * Requires suitable software to open
# * Used for images, audio, video, etc.

# ## Difference Between Text File and Binary File

# Text File:

# * Human-readable
# * Stores characters/text
# * Easy to edit using a text editor
# * Example: `.txt`, `.csv`, `.json`

# Binary File:

# * Not directly human-readable
# * Stores data as bytes
# * Requires suitable software
# * Example: `.jpg`, `.mp3`, `.mp4`

# ## File

# ```text
# File
# │
# ├── Text File
# │   ├── .txt
# │   ├── .csv
# │   ├── .json
# │   ├── .html
# │   ├── .css
# │   ├── .py
# │   └── .xml
# │
# └── Binary File
#     ├── .jpg
#     ├── .png
#     ├── .mp3
#     ├── .mp4
#     ├── .exe
#     └── .pdf
# ```
# # Python : File Opening Modes

# ## 1. Open a File

# To open a file in Python, we use the `open()` function.

# ### Syntax:

# ```python
# f = open(filename, mode)
# ```

# ### Example:

# ```python
# f = open("Users.txt", "r")
# ```

# Here:

# * `f` → File object
# * `"Users.txt"` → File name
# * `"r"` → File opening mode

# # File Opening Modes

# | Mode | Meaning       |
# | ---- | ------------- |
# | `r`  | Read          |
# | `w`  | Write         |
# | `a`  | Append        |
# | `x`  | Create        |
# | `r+` | Read + Write  |
# | `w+` | Read + Write  |
# | `a+` | Read + Append |
# | `rb` | Read Binary   |
# | `wb` | Write Binary  |
# | `ab` | Append Binary |

# ## 1. `r` – Read

# Used to **read** data from a file.

# ```python
# f = open("Users.txt", "r")
# ```

# * File must already exist.
# * If the file does not exist, an error occurs.

# ## 2. `w` – Write

# Used to **write** data to a file.

# ```python
# f = open("Users.txt", "w")
# ```

# * Creates the file if it does not exist.
# * If the file already exists, its old content is **overwritten**.

# ## 3. `a` – Append

# Used to **add new data** at the end of a file.

# ```python
# f = open("Users.txt", "a")
# ```

# * Creates the file if it does not exist.
# * Existing content is not deleted.
# * New data is added at the end.

# ## 4. `x` – Create

# Used to **create a new file**.

# ```python
# f = open("Users.txt", "x")
# ```

# * Creates a new file.
# * If the file already exists, an error occurs.

# # Read + Write Modes

# ## 5. `r+` – Read + Write

# Used for both **reading and writing**.

# ```python
# f = open("Users.txt", "r+")
# ```

# * File must already exist.
# * Existing content is not automatically deleted.

# ## 6. `w+` – Read + Write

# Used for both **reading and writing**.

# ```python
# f = open("Users.txt", "w+")
# ```

# * Creates the file if it does not exist.
# * If the file exists, old content is **deleted/overwritten**.

# ## 7. `a+` – Read + Append

# Used for **reading and appending**.

# ```python
# f = open("Users.txt", "a+")
# ```

# * Creates the file if it does not exist.
# * Existing content is preserved.
# * New data is added at the end.

# # Binary Modes

# ## 8. `rb` – Read Binary

# Used to **read binary data**.

# ```python
# f = open("image.jpg", "rb")
# ```

# ## 9. `wb` – Write Binary

# Used to **write binary data**.

# ```python
# f = open("image.jpg", "wb")
# ```

# ## 10. `ab` – Append Binary

# Used to **append binary data**.

# ```python
# f = open("image.jpg", "ab")
# ```

# # Short Note

# ```text
# r   → Read
# w   → Write
# a   → Append
# x   → Create

# r+  → Read + Write
# w+  → Read + Write
# a+  → Read + Append

# rb  → Read Binary
# wb  → Write Binary
# ab  → Append Binary
# ```
# 2.Read → f.read()
# 3.Close

#Basic Example to read file
# Basic Example to read file

file = open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\Python.txt", "r")

print(file.read())

# content = file.read(8)     # Read first 8 characters
# print(content)

file.close()

# Basic Example to read file using readline()

file = open("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\Python.txt", "r")

# Read one line
print(file.readline(), end="")

print(file.readline(), end="")

print(file.readline(), end="")

print(file.readline(), end="")

file.close()