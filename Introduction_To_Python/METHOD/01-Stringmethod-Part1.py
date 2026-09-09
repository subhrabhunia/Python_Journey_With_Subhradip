a = "Hello, World!"

print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print(a[11])
print(a[12])

# String Slicing
print(a[:5])
print(a[-1:-5:-1])

#for loop
for x in a:
    print(x)

#length method
print(len(a))

#Capitilized method
text="hello world"
result=text.capitalize()
print(result)

#Lower method
texts="HELLO WORLD"
results=texts.lower()
print(results)

#Upper method
word="hello world"
answer=word.upper()
print(answer)

# Title method
name="subhradip Bhunia"
correct_name=name.title()
print(correct_name)

#Find Method
words="python programing language"
print(words.find("python"))
print(words.find("Python")) #No value find
print(words.rfind("g"))
print(words.rfind("o",5))

#Count MEthod
print(words.count("a"))
print(words.count("p"))
print(words.count("o",1))
print(words.count("a",1,3))

#Startswith method
print(words.startswith("python"))
print(words.startswith("Python"))
print(words.startswith("programing", 7))

#Reallife use of Startswith method
url="https://google.com"
if url.startswith(("https://","htpps")):
    print("Valid Url")
else:
    print("Invalid Url")
#endswith
if url.endswith(".com"):
    print("Valid Url")
else:
    print("Invalid Url")


# Strip method
