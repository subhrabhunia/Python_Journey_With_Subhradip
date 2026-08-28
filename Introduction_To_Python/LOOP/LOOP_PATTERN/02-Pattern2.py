#Rverse(Inverted) Right angle pattern:1
for a in range(5,0,-1):
    for b in range(a):
        print("*", end=" ")

    print()

#Rverse(Inverted) Right angle pattern:2
for A in range(5,0,-1):
    for B in range(1,A+1):
        print(B, end=" ")

    print()

#Rverse(Inverted) Right angle pattern:3
for c in range(5,0,-1):
    for d in range(c):
        print(c, end=" ")

    print()

#Rverse(Inverted) Right angle pattern:4
for C in range(5,0,-1):
    for D in range(C,0,-1):
        print(D, end=" ")

    print()

#Rverse(Inverted) Right angle pattern:5
value=1
for e in range(5,0,-1):
    for f in range(e):
        print(value, end=" ")
        

    print()
    value+=1