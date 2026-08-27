#Right Triangle pattern:1
for a in range (1,6):
    for b in range(1,a+1):
        print("*", end=" ")
    print()


#Right Triangle pattern:2
for A in range(1,6):
    for B in range(1,A+1):
        print(B,end=" ")
        B+=1
    print()

#Right Triangle pattern:3
for c in range (1,6):
    for d in range(1,c+1):
        print(c,end=" ")
    print()

#Right Triangle pattern:4
num=1
for C in range (1,6):
    for D in range(1,C+1):
        print(num,end=" ")
        num+=1
    print()