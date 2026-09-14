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