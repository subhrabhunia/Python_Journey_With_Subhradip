#Set Comperehension
numbers=[1,2,2,3,3,4,5]
unique={num for num in numbers}
print(unique)

#Square Value of Set
Numbers=[1,2,3,4,5]
Squares={n**2 for n in Numbers}
print(Squares)

#Tuple Squares
Tuple_Squares=tuple(x*x for x in range(5))
print(Tuple_Squares)

#Dictionary Comprehensions
Dict_Numbers=[1,2,3,4,5]
Square_Dict={Dict:Dict*Dict for Dict in Dict_Numbers}
print(Square_Dict)

#Dictionary With String
Students=["Amit","Rahul","Priya"]
length={Student:len(Student) for Student in Students}
print(length)

#Words Count in List
words=["apple","banana","apple","orange","banana","apple"]
frequency={word:words.count(word) for word in set(words)}
print(frequency)

#Student Grade System
students = [
 ('Ravi',85), ('Tahil', 92), ('Priya', 78),
 ('Sonam', 95), ('Rahul', 88)
]
grade_book={
    name:'A'
    if score>=90 else'B'
    if score>=80 else'C'
    for name,score in students
}
print(grade_book)

#Generator comprehension
gen=(n*n for n in range(5))
print(gen)
print(list(gen))

#Even Numbers only in Gen
Evens_Numbers=(n for n in range (1,21) if n%2==0)
for num in Evens_Numbers:
    print(num)

#String in Gen 
Names=["Amit","Rahul","Priya"]
Upper=(Name.upper() for Name in Names)

# print(list(Upper))

for Name in Upper:
    print(Name)