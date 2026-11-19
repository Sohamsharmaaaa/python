"""Write a python script to accept different types of n values and demonstrate following operations on it:
a) Insert the element at the given position
b) Generate the subset of generated list
c) Display type alongwith the values"""


# function to identify and convert input values
def convert_value(value):
    value = value.strip()
    if value.lower() == "true":
        return True
    elif value.lower() == "false":
        return False
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


# Accept element from the user
n = int(input("Enter the number of elements:: "))
mylist = []
for i in range(n):
    value = input(f"Enter element {i+1}: ")
    mylist.append(convert_value(value))
print("\nOriginal List:", mylist)

# insert an element at a given position
element = input("\nEnter the element to insert:: ")
element = convert_value(element)
position = int(input("Enter the position to insert the element: "))
if 0 <= position <= len(mylist):
    mylist.insert(position, element)
    print("\nList after insertion: ", mylist)
else:
    print("Invalid position")

# generate a subset of the list
start = int(input("\nEnter the starting index for subset:: "))
end = int(input("\nEnter the ending index for subset:: "))
subset = mylist[start:end]
print("\nGenerated substring: ", subset)

# display elements with their data types
print("\nElements with their datatype:")
for item in mylist:
    print(item, "->", type(item).__name__)
