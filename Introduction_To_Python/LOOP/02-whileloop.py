#SYNTAX OF WHILE LOOP
# While Condition:
#      #code to execute       (when that is true)

#While loop flow chart
#         ┌─────────┐
#         │  Start  │
#         └────┬────┘
#              │
#              ▼
#    ┌─────────────────┐
#    │ Initialize      │
#    │ (e.g., i = 1)   │
#    └──────┬──────────┘
#           │
#           ▼
#    ┌─────────────────┐
#    │  Condition?     │
#    │   (i <= n)      │
#    └───┬─────────┬───┘
#        │ Yes     │ No
#        ▼         ▼
# ┌─────────────┐ ┌─────────┐
# │ Execute     │ │   End   │
# │ Statements  │ └─────────┘
# └──────┬──────┘
#        │
#        ▼
# ┌─────────────┐
# │ Update      |
# |(Incriment/  |
# | Decriment)  │
# │ (i = i + 1) │
# └──────┬──────┘
#        │
#        └──────────────► Back to Condition


#Example
a=1
while a<=10:
    print(a);
    a=a+1;

#print 1-5
count=1
while count<=5:
    print(count)
    count=count+1

counts=1
while counts<=20:
    print(counts)
    counts=counts+2

#In reverse
count_reverse=10
while count_reverse>=1:
    print(count_reverse)
    count_reverse=count_reverse-1

#multiplication table
num=8
i=1
while i<=10:
    print(f"{num} X {i} = {num*i}")
    i=i+1

#While else
counting=1
while counting<=6:
    print(counting)
    counting=counting+1
else:
    print("Loop FINISHED")

#In List
fruits=["Apple","Banana","Orange"]
j=0
while j< len(fruits):
    print(fruits[j])
    j+=1


#get user password
password=""
while password !="python123":
    password=input("Entetr password:")
print("Password match")

#Sum of input value
total=0
number=1
while number!=0:
    number=int(input("enter a number (0 to stop)"))
    total+=0
print("Total=",total)