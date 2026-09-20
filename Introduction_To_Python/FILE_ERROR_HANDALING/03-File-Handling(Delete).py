# # Python File Handling

# ## Delete a File

# ### 1. Import

# ```python
# import os
# ```

# `os` is a built-in Python module used to work with files and folders.

# ### 2. Delete

# ```python
# os.remove("data.txt")
# ```

# `os.remove()` is used to delete a file.

# ### Example

# ```python
# import os

# os.remove("data.txt")
# ```

# ### Delete File Using Full Path

# ```python
# import os

# os.remove("D:\\Demo_Python\\data.txt")
# ```

# ### Check File Before Deleting

# ```python
# import os

# if os.path.exists("data.txt"):
#     os.remove("data.txt")
#     print("File deleted successfully")
# else:
#     print("File does not exist")
# ```

# ### Important Functions

# * `import os` → Imports the `os` module.
# * `os.remove()` → Deletes a file.
# * `os.path.exists()` → Checks whether a file or folder exists.

# **Note:** `os.remove()` deletes the specified file.

# Remove File

import os

#os.remove("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\New.txt")

if os.path.exists("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\Test.txt"):

    os.remove("D:\\Demo_Python\\Python_Journey_With_Subhradip\\Introduction_To_Python\\FILE_ERROR_HANDALING\\Test.txt")

    print("File Deleted")

else:

    print("File not Found")