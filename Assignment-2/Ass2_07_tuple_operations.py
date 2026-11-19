"""write a python script to domanstrate following operations on a tuple.
a) Iterate the tuple values
b) Insert a new element in the tuple with a given index
c) sort the given tuple values"""

t1 = (10, 20, 30, 40, 50)
print("Original tuple = ", t1)

index = int(input("enter the position to insert value "))
value = int(input("Enter the value "))
l1 = list(t1)
l1.insert(index, value)
t1 = tuple(l1)
# iterate
for element in t1:
    print(element)

sorted_list = sorted(t1)
t1 = tuple(sorted_list)
print("Sorted tuple = ", t1)
