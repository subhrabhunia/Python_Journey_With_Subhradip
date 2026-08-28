#Left Triangle Pattern:1
rows = 5

for a in range(1, rows + 1):

    # For spaces
    for c in range(rows - a):
        print(" ", end=" ")

    # For stars
    for b in range(a):
        print("*", end=" ")

    print()

#Left Triangle Pattern:2
row = 5
for A in range(1, row + 1):

    # For spaces
    for C in range(row - A):
        print(" ", end=" ")

    # For number
    for B in range(1,A+1):
        print(B, end=" ")

    print()

#Left Triangle Pattern:3
roww = 5
for c in range(1, roww + 1):

    # For spaces
    for d in range(roww - c):
        print(" ", end=" ")

    # For number
    for e in range(1,c+1):
        print(c, end=" ")

    print()

#Left Triangle Pattern:4
row = 5
for C in range(row,0, -1):

    # For spaces
    for D in range(row - C):
        print(" ", end=" ")

    # For number
    for B in range(C):
        print("*", end=" ")

    print()

#Left Triangle Pattern:5
row = 5
for f in range(row,0, -1):

    # For spaces
    for g in range(row - f):
        print(" ", end=" ")

    # For number
    for h in range(1,f+1):
        print(h, end=" ")

    print()

#Left Triangle Pattern:6
row = 5
for F in range(row,0, -1):

    # For spaces
    for G in range(row - F):
        print(" ", end=" ")

    # For number
    for H in range(1,1+F):
        print(F, end=" ")

    print()

#Left Triangle Pattern:7
row = 5
for i in range(row,0, -1):

    # For spaces
    for j in range(0,row - i):
        print(" ", end=" ")

    # For number
    for k in range(i,0,-1):
        print(k, end=" ")

    print()