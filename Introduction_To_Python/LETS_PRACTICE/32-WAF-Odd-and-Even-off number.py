def calculate_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
n=int(input("Enter a number: "))
result = calculate_odd_even(n)
print(f"The number {n} is {result}.")    