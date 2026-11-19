# Write a Python program that reads 5 integers, stores them in a list and handles IndexError and ValueError when the user asks for an element at a given position.
mylist = []
try:
    print("Enter 5 elements:")
    for i in range(5):
        num = int(input("Enter numbers:: "))
        mylist.append(num)
    print("\nList :: ", mylist)

    position = int(input("Enter the position to access (0-4): "))
    print("Elements at position", position, "is: ", mylist[position])
except IndexError:
    print("ERROR: Index out of range! Please enter a position between 0 and 4. ")
except ValueError:
    print("ERROR: Please enter a valid integer. ")
