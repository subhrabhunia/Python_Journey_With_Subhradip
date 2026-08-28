#Hollow Square Pattern
row=5
for a in range(row):
    for b in range(row):
        if a==0 or a==row-1 or b==0 or b==row-1:
         print("*",end=" ")
        else:
         print(" ",end=" ")
    print()


#Pyramid Pattern
roww = 5

for A in range(roww):

    # For spaces
    for C in range(roww - A - 1):
        print(" ", end=" ")

    # For stars
    for B in range(2 * A + 1):
        print("*", end=" ")

    print()

# Hollow Pyramid

row = 5

for d in range(row):

    # For spaces
    for e in range(row - d - 1):
        print(" ", end=" ")

    # For stars
    for f in range(2 * d + 1):

        if f == 0 or f == 2 * d or d == row - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

#X pattern
rows = 7

for i in range(rows):
    for j in range(rows):

        if j == i or j+i == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()