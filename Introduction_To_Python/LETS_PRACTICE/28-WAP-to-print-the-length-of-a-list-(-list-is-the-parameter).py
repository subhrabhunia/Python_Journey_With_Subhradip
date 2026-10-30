Input = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

def length_of_list(Input):
    return len(Input)

print("The length of the list is:", length_of_list(Input))