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