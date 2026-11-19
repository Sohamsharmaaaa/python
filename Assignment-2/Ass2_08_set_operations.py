"""write a python script to demonstrate operations on set such as creating a set, adding new value, remove the value and popping the value"""

n = int(input("Enter n"))
myset = set()
print(f"enter {n} unique values  :")
for i in range(n):
    myset.add(int(input()))
print("Original set ", myset)

value = int(input("Enter value to remove "))
myset.discard(value)
print("Set after remove ", myset)

try:
    print("popped value is ", myset.pop())
except KeyError:
    print("Set is Empty")
