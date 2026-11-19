"""Write a python program to add student records(rollno, name, marks) into a binary file. Write a code to
search a particular roll number and to display all records."""

import pickle

FILE = "students.dat"
# add records
n = int(input("How many records to add: "))
with open(FILE, "ab") as f:
    for _ in range(n):
        roll = int(input("Roll no: "))
        name = input("Name: ")
        marks = float(input("Marks: "))
        pickle.dump({"roll": roll, "name": name, "marks": marks}, f)

# display all records
print("\nAll records: ")
with open(FILE, "rb") as f:
    while True:
        try:
            r = pickle.load(f)
            print(r["roll"], r["name"], r["marks"])
        except EOFError:
            break

# search record
search_roll = int(input("\nEnter roll no to search: "))
found = False
with open(FILE, "rb") as f:
    while True:
        try:
            r = pickle.load(f)
            if r["roll"] == search_roll:
                print("Found:", r["roll"], r["name"], r["marks"])
                found = True
                break
        except EOFError:
            break
if not found:
    print("Record not found.")
