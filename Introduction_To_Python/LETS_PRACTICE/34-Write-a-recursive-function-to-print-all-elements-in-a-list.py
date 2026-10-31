def print_list(list,index):
    if index == len(list):
        return
    print(list[index])
    print_list(list,index+1)
fruits=["apple","banana","cherry","date"]
print_list(fruits,0)