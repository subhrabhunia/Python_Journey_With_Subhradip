#Hollow Square Pattern
row=5
for a in range(row):
    for b in range(row):
        if a==0 or a==row-1 or b==0 or b==row-1:
         print("*",end=" ")
        else:
         print(" ",end=" ")
    print()