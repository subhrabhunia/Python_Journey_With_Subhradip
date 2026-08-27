# #Example
# for i in range(1,11):
#     if i == 5:
#         break
#     print(i)
# print("Loop Finished")

# #IN list
# fruits = ["Apple", "Banana", "Orange", "Mango"]

# search = "Banana"

# for fruit in fruits:
#     if fruit == search:
#         print("Fruit Found")
#         break
# else:
#     print("Not Found")  #This working when the item not found in the list
# print("Search Completed")

#pin Mannagement
correct_pin = "1234"

while True:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Log in Successful.")
        break

    print("Incorrect PIN")