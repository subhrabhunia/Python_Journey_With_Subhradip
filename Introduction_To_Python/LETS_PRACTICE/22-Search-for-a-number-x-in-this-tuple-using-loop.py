nums=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x=int(input("Enter a number to search in the tuple: "))
i=0
while i<len(nums):
    if nums[i]==x:
        print("Number",x,"found at index",i)
        break
    i+=1