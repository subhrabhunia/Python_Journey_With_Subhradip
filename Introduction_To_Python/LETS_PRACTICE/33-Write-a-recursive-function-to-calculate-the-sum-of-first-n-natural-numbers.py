def cal_sum(n):
    if n == 0:
        return 0  # Fixed: Must return 0 instead of None
    return cal_sum(n-1) + n

n = int(input("Enter a number: "))
total_sum = cal_sum(n)
print("The sum of first", n, "natural numbers is:", total_sum)
