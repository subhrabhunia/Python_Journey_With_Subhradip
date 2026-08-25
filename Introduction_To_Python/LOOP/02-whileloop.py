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