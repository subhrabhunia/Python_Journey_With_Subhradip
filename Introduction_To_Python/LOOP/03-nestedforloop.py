# SYNTAX OF NESTED FOR LOOP 
# for varriable in sequence:
#     for variable in sequence:
#         #code execute

# WHERE WE USE NESTED FOR LOOP:
# 1.Processing rows and collumn data.
# 2.Matrix operations(addition,multiplication,transpose).
# 3.Printing Patterns(stars,numbers,pyramids).
# 4.Seating arrangements(cinema,classroom,bus).
# 5.Game development(2D grids and maps).
# 6.Comparing items from two collections.

#Print a  square 
for i in range(5):    #outer loops
    for j in range(5):   #inner loops
        print("*",end="  ")  #END USE TO EMPTY SPACE>
    print( )  #Enter in next line and enter in outer loops.

#Print 1 to 100 
rows=10
num=1
for k in range(rows):
    for l in range(rows):
        print(num,end=" ")
        num=num+1
    print()

#Triangle pattern
for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

#student table
stuedents=["Amit","Riya","Rahul"]
Subjects=["Math","Science","English"]
for student in stuedents:
    print(f"\nMarks of {student}")
    for subject in Subjects:
        print(subject)


StName = ["Amit", "Riya", "Rahul"]

SuName = [
    {"Math": 67, "Science": 43, "English": 86},
    {"Math": 77, "Science": 56, "English": 78},
    {"Math": 67, "Science": 90, "English": 95},
]

for St, marks in zip(StName, SuName):

    print(f"\nMarks of {St}")

    for Su, mark in marks.items():
        print(f"{Su}: {mark}")