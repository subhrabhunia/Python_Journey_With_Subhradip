#add
def add(a,b):
    result=a+b
    return result
sum=add(10,20)
print(sum)

#Chech even
def check_even(number):
    if number%2==0:
       return "Even"
    else:
        return"Odd"
print(check_even(15))
print(check_even(12))

#Total sum
def total(numbers):
    results = 0

    for num in numbers:
        results += num

    return results


marks = [20, 50, 40, 30]

print(total(marks))