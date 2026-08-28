#Left Triangle Pattern:1
rows = 5

for a in range(1, rows + 1):

    # For spaces
    for c in range(rows - a):
        print(" ", end="")

    # For stars
    for b in range(a):
        print("*", end=" ")

    print()