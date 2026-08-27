# SYNTAX OF NESTEDWHILE LOOP:-
# while condition:
#     while condition:
#         code to execute.

#Square pattern
i=1
while i<=5:
    j=1
    while j<=5:
        print("*",end=" ")
        j+=1
    print()
    i+=1

#Multiplication table
num=1
while num <= 5:
    k=1
    while k<=10:
        print(f"{num} X {k} ={num*k}")
        k+=1
    print("-"*20)
    num+=1


#TICTAC GAME
board=[
    ["X", "O", "X"],
    ["O", "X", "X"],
    ["X", "O", "X"]   
]
l=0
while l<len(board):
    m=0
    while m<len(board[l]):
        print(board[l][m],end=" ")
        m+=1
    print()
    l+=1

#Student Table
StName = ["Amit", "Riya", "Rahul"]

Marks = [
    {"Math": 67, "Science": 43, "English": 86},
    {"Math": 77, "Science": 56, "English": 78},
    {"Math": 67, "Science": 90, "English": 95},
]
n=0
while n<len(StName):
    print("Student Name:",StName[n])
    Subjects=list(Marks[n].items())
    p=0
    while p<3:
        Subject,Score=Subjects[p]
        print(Subject,":",Score)
        p+=1
    print("-"*20)

    n+=1