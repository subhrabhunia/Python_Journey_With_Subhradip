with open("practice.txt", "w") as file:
    file.write("Hi everyone\nwe are learning File I/0\n")
    file.write("using Java. \nI like programming in Java. ")
file.close()

# Q2. Write a function that replaces all occurrences of "java"
def replace_java():
    with open("practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("Java", "Python")

    with open("practice.txt", "w") as f:
        f.write(new_data)


replace_java()

with open("practice.txt", "r") as f:
    print(f.read())


# Q3. Search if the word "learning" exists in the file or not.
word = "learning"

with open("practice.txt", "r") as f:
    data = f.read()

if word in data:
    print("Found")
else:
    print("Not found")

# Q4. Write a function to find in which line of the file the word
def check_line(word):
    line_no = 1

    with open("practice.txt", "r") as f:
        # Reads one line at a time
        for line in f:
            if word in line:
                return line_no

            line_no += 1

    return -1


print(check_line("learning"))
print(check_line("hello"))

# Q5. From a file containing numbers separated by commas,
pcount = 0

with open("numbers.txt", "r") as f:
    data = f.read()

nums = data.split(",")

for num in nums:
    if int(num) % 2 == 0:
        count += 1

# List of strings

print("Even numbers:", count)