#Example
for i in range(1,11):
    if i==5:
        continue
    print(i)

#print odd number
for j in range(1,11):
    if j%2==0:
        continue
    print(j)

#List
Names=["Ram","","Riya","","Rahul"]
for name in Names:
    if name=="":
        continue
    print(name)

#Marks Table
marks=[75,85,90,29,35]
for mark in marks:
    if mark<40:
        continue
    print(mark)


#skip vowels
word="PYTHON"
for letter in word:
    if letter in "AEIOU":
        continue
    print(letter)