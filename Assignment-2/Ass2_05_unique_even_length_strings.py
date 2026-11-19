# Write a python script to accept 'n' strings from user and display all even length strings. Do not accept duplicate strings.
n = int(input("Enter number of strings:: "))
mystr = set()
print(f"Enter {n} Strings:: ")
while len(mystr) < n:
    temp = input(f"String {len(mystr)+1}:: ")
    if temp in mystr:
        print("Duplicate string are not allowed. Please enter a unique string.")
    else:
        mystr.add(temp)

print("\nEven length string::")
for string in mystr:
    if len(string) % 2 == 0:
        print(f" - {string} (length:  {len(string)})")
