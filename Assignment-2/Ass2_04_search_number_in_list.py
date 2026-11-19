# Write a python script to accept n values from user and store it into a list. Accept a number from user and check whether it is present in the list or not.
n = int(input("Enter no. of values to store in a list"))
mylist = []
print(f"Enter {n} values:: ")
for i in range(n):
    val = input(f"Enter {i+1}:: ")
    mylist.append(val)

search = input("Enter the number to be searched:: ")
if search in mylist:
    print(search, " is present in the list")
else:
    print(search, " not present in the list")
