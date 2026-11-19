# Python Practical Programs

A collection of **35 Python practical programs** organised assignment-wise. The programs move from core
Python fundamentals through data structures, file handling and data analysis, and into practical
networking, web and cryptography tasks — so the set doubles as a gentle **Python-for-cybersecurity**
practical course.

The full source code of every program is listed in this README (grouped by assignment), and each program
also lives as a runnable `.py` file in its `Assignment-*` folder.

## Repository structure

```
python/
├── Assignment-1/   Python fundamentals (conditionals, functions, NumPy matrices)
├── Assignment-2/   Data structures & exception handling
├── Assignment-3/   File handling, serialization & data analysis (pandas / matplotlib)
├── Assignment-4/   Networking & web (requests, BeautifulSoup, Scapy, nmap)
├── Assignment-5/   Hashing & cryptography (hashlib, PBKDF2, Fernet)
├── requirements.txt
└── README.md
```

## How to run

```bash
git clone https://github.com/Sohamsharmaaaa/python.git
cd python
python -m venv .venv
# Windows:  .venv\Scripts\activate     Linux/macOS:  source .venv/bin/activate
pip install -r requirements.txt
python Assignment-1/Ass1_07_password_strength_score.py
```

Most programs are interactive (they read input from the keyboard). A few need a data file or a running
local server — those notes are in each program's comments. The third-party libraries used (numpy, faker,
pandas, matplotlib, requests, beautifulsoup4, scapy, python-nmap, cryptography) are in
[`requirements.txt`](requirements.txt).

---

## Contents

- [Assignment 1 — Python Fundamentals](#assignment-1-python-fundamentals)
- [Assignment 2 — Data Structures & Exception Handling](#assignment-2-data-structures-exception-handling)
- [Assignment 3 — File Handling & Data Analysis](#assignment-3-file-handling-data-analysis)
- [Assignment 4 — Networking & Web](#assignment-4-networking-web)
- [Assignment 5 — Hashing & Cryptography](#assignment-5-hashing-cryptography)

---


## Assignment 1 — Python Fundamentals

### 1. `Ass1_04_public_private_ip_check.py`

Checks whether an entered IPv4 address is **private** or **public**.

```python
i# Write a python program to check the given ip address is public or private

ip = input("Enter the ip address")
ipstr = ip.split(".")
flag = False
if len(ipstr) != 4:
    print("Wrong IP Address")
else:
    first = int(ipstr[0])
    second = int(ipstr[1])
    print(first, second)
    if first == 172 and (second >= 16 and second <= 31):
        flag = True
    elif first == 192 and second == 168:
        flag = True
    else:
        pass
    if flag == True:
        print("Private IP Address")
    else:
        print("Publc IP Address")
```

### 2. `Ass1_05_file_extension_warning.py`

Reads a filename and prints a message based on its extension using `match`/`case`.

```python
# Write a program to accept the filename, check the extension of it and show the appropriate warning message
filename = input("Enter the filename:: ")
ext = filename.split(".")
if len(ext) != 2:
    print("Wrong Filename")
else:
    match ext[1]:
        case "exe" | "out":
            print("this ia an executable file")
        case "txt":
            print("This is a text file")
        case "pdf":
            print("This is a pdf file")
        case "ppt":
            print("This is a ppt")
        case "docx":
            print("this is a document")
        case "py":
            print("Ths is apython file")
        case _:
            print("Unknown filename")
```

### 3. `Ass1_06_role_based_access_control.py`

Role-based access control — grant / restrict / deny based on role and authentication state.

```python
# Write a program to determine whether a user should be granted, denied or restricted access based to role and authentication states.

users = {"Jayesh": "admin", "Jay": "analyst", "Yash": "user", "Samay": "user"}
name = input("Enter your name:").lower()
authenticated = input("Are you authenticated? (yes/no): ").lower()

if name not in users:
    print("Access Denied: user not registered.")
elif authenticated == "no":
    print("Access Denied: user is not authenticated.")
elif authenticated == "yes":
    role = users[name]
    match role:
        case "admin":
            print("Access Granted: Full system access.")
        case "analyst":
            print("Access Restricted: Security analysis access only.")
        case "user":
            print("Access Restricted: Limited user access.")
        case _:
            print("Access Denied: Unknown role.")
else:
    print("invalid authentication status.")
```

### 4. `Ass1_07_password_strength_score.py`

Scores a password on length, case, digits and symbols and classifies it **weak / medium / strong**.

```python
# write a python progran using function to calculate the security score of a pass word. Assign points based on password length, uppercase letters, lowercase letters, digits and special characters. Display the total score and classify the passwordas weak, medium, strong.

import string


def calculate_score(password):
    score = 0
    # check password length
    if len(password) >= 8:
        score += 2
    elif len(password) >= 6:
        score += 1  
    # check for uppercase latter
    if any(char.isupper() for char in password):
        score += 2
    # check for lowercase letter
    if any(char.islower() for char in password):
        score += 2
    # check for special character
    if any(not char.isalnum() for char in password):
        score += 2
    return score


def classify_password(score):
    if score <= 4:
        return "weak"
    elif score <= 7:
        return "medium"
    else:
        return "strong"


password = input("enter your password: ")
score = calculate_score(password)
strength = classify_password(score)
print("security score:", score)
print("password strength:", strength)
```

### 5. `Ass1_09_matrix_operations.py`

Menu-driven NumPy matrix tool — addition, multiplication, triangular and symmetric checks.

```python
"""write a python script to accept two matrices and perform following opperation on it:-
1.addition
2.multiplication
3.check whether the first matrix is upper triangular
4. check whether the second matrix is lower trangular
5.check first matrix is symmetric"""

import numpy as np

d = int(input("Enter the dimension of the matrix: "))
print("Enter first matrix", d * d, "values separated by one space:")
input_str = input()
arr = np.fromstring(input_str, dtype=float, sep=" ")
if len(arr) != d * d:
    print("Wrong number of values for first matrix")
else:
    print("Enter second matrix", d * d, "values separated by one space:")
    input_str1 = input()
    arr1 = np.fromstring(input_str1, dtype=float, sep=" ")
    if len(arr1) != d * d:
        print("Wrong number of values for second matrix")
    else:
        mat1 = arr.reshape((d, d))
        mat2 = arr1.reshape((d, d))
        print("\nFirst Matrix:")
        print(mat1)
        print("\nSecond Matrix:")
        print(mat2)
        while True:
            print("\n----- MENU -----")
            print(
                "1. Addition\n2. Multiplication\n3. Check first matrix is Upper Triangular\n4. Check second matrix is Lower Triangular\n5. Check first matrix is Symmetric\n6.exit"
            )
            ch = int(input("Enter your choice: "))
            match ch:
                case 1:
                    print("\nAddition:")
                    print(mat1 + mat2)
                case 2:
                    print("\nMultiplication:")
                    print(mat1 @ mat2)
                case 3:
                    flag = True
                    for i in range(d):
                        for j in range(d):
                            if i > j:
                                if mat1[i][j] != 0:
                                    flag = False
                    if flag:
                        print("First matrix is Upper Triangular")
                    else:
                        print("First matrix is NOT Upper Triangular")
                case 4:
                    flag = True
                    for i in range(d):
                        for j in range(d):
                            if i < j:
                                if mat2[i][j] != 0:
                                    flag = False
                    if flag:
                        print("Second matrix is Lower Triangular")
                    else:
                        print("Second matrix is NOT Lower Triangular")
                case 5:
                    flag = True
                    for i in range(d):
                        for j in range(d):

                            if mat1[i][j] != mat1[j][i]:
                                flag = False
                    if flag:
                        print("First matrix is Symmetric")
                    else:
                        print("First matrix is NOT Symmetric")
                case 6:
                    print("Program ended")
                    break
                case _:
                    print("Invalid choice")
```

### 6. `Ass1_10_matrix_inverse_check.py`

Accepts two matrices and checks whether the second is the **inverse** of the first.

```python
# Accept two matrices and check whether second is inverse of first matrix
import numpy as np

d = int(input("enter the dimention of the matrix: "))
print("enter first matrix", d * d, "value seprated by one space: ")
input_str = input()
arr = np.fromstring(input_str, dtype=float, sep=" ")
if len(arr) != (d * d):
    print("wrong no. of values for first matrix")
else:
    print("enter second matrix", d * d, "value seprated by one space:")
    input_str1 = input()
    arr1 = np.fromstring(input_str1, dtype=float, sep=" ")
    if len(arr1) != (d * d):
        print("wrong no. of values in second matrix")
    else:
        mat1 = arr.reshape((d, d))
        mat2 = arr1.reshape((d, d))
        print(mat1)
        print(mat2)
        iden = np.identity(d)
        if np.allclose(mat1 @ mat2, iden):
            print("second matrix is inverse of first")
        else:
            print("second matrix is not inverse of first")

"""
enter the dimention of the matrix: 2
enter first matrix 4 value seprated by one space:
4 2 1 3
enter second matrix 4 value seprated by one space:
0.3 -0.2 -0.1 0.4
[[4. 2.]
 [1. 3.]]
[[ 0.3 -0.2]
 [-0.1  0.4]]
second matrix is inverse of first
"""
```

---

## Assignment 2 — Data Structures & Exception Handling

### 1. `Ass2_02_constant_time_password_comparison.py`

Constant-time password / API-key comparison to resist **timing attacks**.

```python
# Write a constant time password verifier function to defend against timing attack. Use this function to safely compare user supplied API keys or passwords against stored ones.


def secure_compare(stored: str, userinput: str) -> bool:
    if len(stored) != len(userinput):
        target = stored
        len_result = 1
    else:
        target = userinput
        len_result = 0
    content_result = 0
    for ch1, ch2 in zip(stored, target):
        content_result |= ord(ch1) ^ ord(ch2)
    return (len_result | content_result) == 0


actual_hash = "Indira123"
input_hash = input("Enter the input password or ap key:: ")
print(secure_compare(actual_hash, input_hash))
```

### 2. `Ass2_04_search_number_in_list.py`

Stores `n` values in a list and searches for a value.

```python
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
```

### 3. `Ass2_05_unique_even_length_strings.py`

Collects unique strings in a `set` and prints the even-length ones.

```python
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
```

### 4. `Ass2_06_mixed_type_list_operations.py`

Mixed-type list — insert at a position, slice a subset and print each value's type.

```python
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
```

### 5. `Ass2_07_tuple_operations.py`

Iterate, insert into and sort a tuple.

```python
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
```

### 6. `Ass2_08_set_operations.py`

Create / add / discard / pop operations on a `set`.

```python
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
```

### 7. `Ass2_09_compare_server_ports_with_sets.py`

Compares two servers' open ports using set union / intersection / difference.

```python
"""Write a python program to create two sets of open ports if two servers and display the union,
intersection and difference of the sets."""

server1 = {21, 22, 80, 443, 3306, 8080}
server2 = {22, 25, 80, 443, 5432, 8443}
print("server 1 open ports : ", sorted(server1))
print("Server 2 open ports : ", sorted(server2))
print()

# union: ports open on at least one server
union_ports = server1 | server2
print("Union (open on either server) : ", sorted(union_ports))

# intersection: ports open on both servers
common_ports = server1 & server2
print("\nIntersection (open on both servers) : ", sorted(common_ports))

# Difference: ports open on one sers but not on other
only_server1 = server1 - server2
only_server2 = server2 - server1
print("\nDifference (server 1 - server 2) : ", sorted(only_server1))
print("\nDifference (server 2 - server 1) : ", sorted(only_server2))

# Symmetric difference: ports open exactly one of the servers
print("\nSymmetric difference: ", sorted(server1 ^ server2))
```

### 8. `Ass2_10_word_frequency_counter.py`

Word-frequency counter with a dictionary; reports the most frequent word(s).

```python
"""Write a python program to accept a sentence, and using a dictionary display the frequency of each word. Also display the most frequent word."""

import string


def word_frequency(sentence):
    cleaned = sentence.lower().translate(str.maketrans("", "", string.punctuation))
    freq = {}
    for word in cleaned.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


sentence = input("Enter a sentence: ").strip()
if not sentence:
    print("No sentence entered ")
else:
    freq = word_frequency(sentence)
    if not freq:
        print("No words found ")
    else:
        print("\nWord frequencies:")
for word, count in sorted(freq.items(), key=lambda item: item[1], reverse=True):
    print(f"{word:<15} : {count}")

# most frequent word(s): handle ties by collecting every word with max count
max_count = max(freq.values())
top_words = [word for word, count in freq.items() if count == max_count]
print()
if len(top_words) == 1:
    print(f"Most frequent word: '{top_words[0]}' (appears {max_count} time.)")
else:
    print(f"Most frequent words (tie, {max_count} times each):{', '.join(top_words)}")
```

### 9. `Ass2_11_failed_login_ip_frequency.py`

Generates fake failed-login IPs with **Faker** and flags IPs with more than 3 attempts.

```python
# write a python program that generates a list of IP address (with repetitions) of failed login attempts using faker and uses a dictionary to diaplay the number of attempts per IP. display IPs having more than 3 attempts as 'suspicious'.

import random
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)


def generate_failed_logins(num_ips=6, total_attempts=25):
    # generate a list of IPs with repetitions using faker. create a small pool of unique fake IP then sample from it with repetition so that some IPs appear manytimes.
    ip_pool = [fake.ipv4() for _ in range(num_ips)]
    return random.choices(ip_pool, k=total_attempts)


def count_attempts(ip_list):
    # return a dictionary mapping each IP to its number of failed attempts.
    attempts = {}
    for ip in ip_list:
        attempts[ip] = attempts.get(ip, 0) + 1
    return attempts


failed_logins = generate_failed_logins()
print("Generated failed login attempts: ")
print(failed_logins)

attempts = count_attempts(failed_logins)

print("\nFailed login attempts per  IP: ")
for ip, count in sorted(attempts.items(), key=lambda item: item[1], reverse=True):
    status = "SUSPICIOUS" if count > 3 else ""
    print(f"{ip:<16} : {count:>2} attempt(s) {status}")

print("\nSuspicious IPs (more than 3 attempts) : ")
suspicious = {ip: count for ip, count in attempts.items() if count > 3}
if suspicious:
    for ip, count in suspicious.items():
        print(f" {ip} -> {count} attempts")
else:
    print("None")

# to install faker ---- pip install faker --break-system-packages
```

### 10. `Ass2_12_list_index_error_handling.py`

Reads 5 integers and handles `IndexError` / `ValueError` on access.

```python
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
```

### 11. `Ass2_13_network_port_validation.py`

`parse_port()` validates a port (1–65535) using `try`/`except`/`finally`.

```python
# Write a function parse_port(value) that takes a string from user input and returns it as an integer port number. If the string is not a valid integer, catch the ValueError and print "Invalid port: not a number". If the number is outside the range 1-65535, raise a exception with a meaningful message and handle it in the caller. Use a finally block to print "Validation complete" regardless of the outcome.


def parse_port(value):
    try:
        port = int(value)
    except ValueError:
        raise ValueError("Invalid port: NOt a number")
    if port < 1 or port > 65535:
        raise Exception("Port number must be between 1 and 65535")
    return port


try:
    port = input("Enter port number: ")
    result = parse_port(port)
    print("Valid port number: ", result)
except ValueError as e:
    print(e)
finally:
    print("Validation complete")
```

### 12. `Ass2_14_authentication_log_analysis.py`

Parses an auth log, validates IPs/timestamps, counts failed logins per IP and logs skipped lines.

```python
"""
Build a tool to analyze authentication logs. Each line has the format:
        2026-10-27 09:15:32,192.168.1.10,LOGIN_FAILED,admin
Write a python script that reads a log file and counts failed login attempts per IP address.
1. Handle FileNotFoundError and PermissionError separately, with different messages.
2. Malformed lines (wrong number of fields, invalid IP format, unparseable timestamp) must not crash the program.
   Log them to a separate list with the line number and the reason, then continue processing.
3. Use ipaddress.ip_address() to validate IPs and catch the exception it raises.
4. Use the with statement for file handling.
5. At the end, print the offending IPs and a summary of how many lines were skipped.
"""

"""
sample_auth.log file 

2026-10-27 09:15:32,192.168.1.10,LOGIN_FAILED,admin
2026-10-27 09:15:40,192.168.1.10,LOGIN_FAILED,root
2026-10-27 09:16:01,10.0.0.5,LOGIN_OK,akash
2026-10-27 09:16:15,10.0.0.99,LOGIN_FAILED,sarika
2026-10-27 09:17:00,999.1.1.1,LOGIN_FAILED,admin
2026-10-27 25:99:00,10.0.0.99,LOGIN_FAILED,sarika
only,two,fields
2026-10-27 09:18:00,10.0.0.99,LOGIN_FAILED,sameer

"""

import ipaddress
import sys
from collections import Counter
from datetime import datetime


# Return (timestamp, ip, event, user) or raise ValueError with a error message.
def parse_line(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 4:
        raise ValueError(f"expected 4 fields, got {len(parts)}")
    ts, ip, event, user = parts
    try:
        datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(f"unparseable timestamp '{ts}'")
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise ValueError(f"invalid IP address '{ip}'")
    return ts, ip, event, user


def analyze(filename):
    failed = Counter()
    skipped = []  # contains tuple (line_number, reason)
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    _, ip, event, _ = parse_line(line)
                except ValueError as e:
                    skipped.append((lineno, str(e)))
                    continue
                if event == "LOGIN_FAILED":
                    failed[ip] += 1
    except FileNotFoundError:
        print(f"Error: file '{filename}' does not exist.")
        return
    except PermissionError:
        print(f"Error: no permission to read '{filename}'.")
        return
    except UnicodeDecodeError as e:
        print(f"Error: file is not valid UTF-8 ({e.reason}).")
        return

    print("Offending IPs:")
    for ip, count in failed.items():
        print(f"{ip} ----> {count} failed attempts")
    print(f"\nSkipped lines are: {len(skipped)}")
    for lineno, reason in skipped:
        print(f"line {lineno}: {reason}")


# main block ---- command line argument
analyze(sys.argv[1] if len(sys.argv) > 1 else "auth.log")

""" 
execute as follows on $ prompt
$python Ass2_exception_log_analyzer.py sample_auth.log
"""
```

---

## Assignment 3 — File Handling & Data Analysis

### 1. `Ass3_01_malicious_word_search.py`

Scans a file for suspicious keywords and reports their line numbers.

```python
"""Write a python script to open a file and check wether it contains a malicious word. Display the
malicious word and the line numbers containing that word."""

malicious_words = [
    "malware",
    "virus",
    "trojan",
    "ransomware",
    "exploit",
    "phishing",
    "password",
    "account",
    "hack",
]

filename = input("Enter file name: ")
found = {}
try:
    with open(filename, "r") as file:
        for line_no, line in enumerate(file, start=1):
            for word in malicious_words:
                if word in line.lower():
                    if word not in found:
                        found[word] = []
                    found[word].append(line_no)
    for word, lines in found.items():
        print(f"{word}: {lines}")
except FileNotFoundError:
    print("File does not exists....")
```

### 2. `Ass3_02_dictionary_text_compression.py`

Compresses a file by replacing repeated words with symbols, plus a dictionary legend.

```python
"""Write a python script to input a filename and generate the another compressed file by replacing the
duplicate words with a single special character. Also add the dictionary at the end of the compressed
file as replaced_word: special symbol"""

filename = input("Enter file name ")
# Read the file and collect the words
with open(filename, "r") as file:
    lines = file.readlines()

# count how often each word appears
count = {}
for line in lines:
    for word in line.split():
        count[word] = count.get(word, 0) + 1

# Give each duplicat word a special symbol
symbols = {}
code = 0x2600  # start of the unicode " Miscellaneous Symbols" block
for word, c in count.items():
    if c > 1:
        symbols[word] = chr(code)
        code += 1

# write the compressed file
output_name = "compressed_" + filename
with open(output_name, "w", encoding="utf-8") as out:
    for line in lines:
        new_words = [symbols.get(word, word) for word in line.split()]
        out.write(" ".join(new_words) + "\n")

        # Add the dictionary at the end
    out.write("\n----- Dictionary ------------\n")
    for word, symbol in symbols.items():
        out.write(f"{word} : {symbol}\n")
print("Compressed file created: ", output_name)
```

### 3. `Ass3_03_student_records_pickle.py`

Stores student records in a binary file with **pickle**, then displays and searches them.

```python
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
```

### 4. `Ass3_06_fake_login_records_csv.py`

Generates 50 fake login records with **Faker** and writes them to a CSV (shown via pandas).

```python
"""using Faker, generate a csv file of 50 fake login records (time, username, ip, status) and display the
first 10 rows using pandas"""

from faker import Faker
import pandas as pd
import random

fake = Faker()
records = []
for _ in range(50):
    records.append(
        {
            "time": fake.date_time_this_month(),
            "username": fake.user_name(),
            "ip": fake.ipv4(),
            "status": random.choice(["success", "failed"]),
        }
    )
df = pd.DataFrame(records)
df.to_csv("login_records.csv", index=False)
print(df.head(20))
```

### 5. `Ass3_07_top_failed_login_ips_chart.py`

Finds the top-5 IPs by failed logins and saves a **bar chart**. *(Run `Ass3_06` first.)*

```python
"""write a python script using pandas, find the top 5 ip addresses having the most failed logins and plot
them as a bar chart. Save the chart as an image"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("login_records.csv")

# Keep only failed and count them per ip
failed = df[df["status"] == "failed"]
top5 = failed["ip"].value_counts().head(5)
print(top5)

# plot as a bar chart and save as an image
top5.plot(kind="bar", color="blue")
plt.title("Top 5 IPs with Most failed logins")
plt.xlabel("IP Address")
plt.ylabel("failed logins")
plt.tight_layout()
plt.savefig("top5_failed_ips.png")
plt.show()
```

### 6. `Ass3_08_failed_logins_by_hour_chart.py`

Finds the busiest hour for failed logins and saves a **line chart**. *(Run `Ass3_06` first.)*

```python
"""write a python script using pandas, find the hour of the day in which th maximum number of failed login
occur and plot a line chart of failed logins per hour."""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("login_records.csv")

# Keep only failed logins and count time per IP
failed = df[df["status"] == "failed"]
failed["time"] = pd.to_datetime(failed["time"])

hourly_counts = failed.groupby(failed["time"].dt.hour).size()
max_count = max(hourly_counts)
max_count_hours = hourly_counts[hourly_counts == max_count]
for h, count in max_count_hours.to_dict().items():
    print(f"{h} hour has {count} times failed attempts")

# plot as a line chart a save as an image
hourly_counts.plot(color="blue")
plt.title("Hour-wise no. of failed attempts")
plt.xlabel("hour")
plt.ylabel("failed logins")
plt.tight_layout()
plt.savefig("hourwise_failed_attempts.png")
plt.show()
```

---

## Assignment 4 — Networking & Web

### 1. `Ass4_prog01_fetch_web_page_metadata.py`

Fetches a page with **requests** and prints status code, headers and page size.

```python
# Write a Python program using requests to fetch a web page (a local test page) and display the status code, response headers and the page size.

import requests

response = requests.get("http://127.0.0.1:8000/index.html")

print("Status code:", response.status_code)

print("\nResponse headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")

print("\nPage size:", len(response.content), "bytes")

"""
Steps to run:
1. Start the default python server by giving command on terminal as
    $python3 -m http.server  
       OR 
    if we want to use different port no than default(8000)
    $python3 -m http.server 8080
    Note that donot close this terminal.
2. Create a html file in the same folder as index.html may be blank or
   add some html contents like 
     	<html>
	<body>
	<h1>Hello to all
	</body>
	</html>
3. Then open the firefox browser and type url as:
	http://localhost:8000
   We will see the output displayed on browser as:
   	Hello to all
4. Run the python program on another terminal as:
	$python program_name.py
5. At the end stop the server by pressing ctrl+c
"""
```

### 2. `Ass4_prog02_extract_html_title_and_links.py`

Uses **BeautifulSoup** to extract a page's title and all hyperlinks.

```python
# Write a Python program using BeautifulSoup to extract and display the title and all hyperlinks of a given HTML page.

import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:8000/index.html"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
if soup.title:
    print("Title:", soup.title.string)
else:
    print("No title tag found in this HTML.")

print("\nHyperlinks:")
for link in soup.find_all("a"):
    print(link.get("href"))

""" 
index.html

<html>
<title> This is my first page</title>
<body>
<h1>Hello to all
<a href="next.html"> Next
<a href="previous.html">Previous
</body>
</html>
"""
```

### 3. `Ass4_prog04_send_icmp_echo_request.py`

Builds and sends an ICMP echo request to `127.0.0.1` with **Scapy**. *(Needs admin/root.)*

```python
# Write a Python program using Scapy to create an ICMP echo request packet for 127.0.0.1, display its layers using show()  and send it.

from scapy.all import IP, ICMP, send, sr1

# Build the ICMP echo request (ping) packet for localhost
packet = IP(dst="127.0.0.1") / ICMP()

# Display the packet's layers and field values
print("=== Packet layers ===")
packet.show()

# Send the packet (layer 3, no reply handling)
print("\n=== Sending packet ===")
send(packet)
```

### 4. `Ass4_prog06_extract_emails_and_form_fields.py`

Extracts emails (regex) and form field names (BeautifulSoup) from a local HTML page to a CSV.

```python
# Write a Python program to extract all the e-mail addresses and all form input field names from a given local HTML page
# using Beautiful Soup and regular expressions. Save the output to a CSV file.

import re
import csv
from bs4 import BeautifulSoup

# Read the local HTML file
filename = input("Enter HTML file name: ")
with open(filename, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Find all email addresses using a regular expression
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
emails = set(re.findall(email_pattern, html))

# Find all form input field names
input_names = []
for tag in soup.find_all("input"):
    name = tag.get("name")
    if name:
        input_names.append(name)

# Save to CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Type", "Value"])
    for e in emails:
        writer.writerow(["Email", e])
    for n in input_names:
        writer.writerow(["Input Name", n])

print("Emails found:", emails)
print("Input names found:", input_names)
print("Saved to output.csv")

"""
To run this script, first create html file having some email ids and a form containing input fields such as text box, 
radio button, checkbox, etc.

Sample html file is : test.html

<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <h1>Contact Us</h1>

    <p>For general queries, write to info@example.com</p>
    <p>For support, email support@mysite.org or sales.team@company.co.in</p>
    <p>Click here: <a href="mailto:admin@example.com">Email Admin</a></p>

    <form action="/submit" method="post">
        <label>Name:</label>
        <input type="text" name="username"><br>

        <label>Email:</label>
        <input type="email" name="user_email"><br>

        <label>Password:</label>
        <input type="password" name="user_password"><br>

        <label>Age:</label>
        <input type="number" name="age"><br>

        <label>Gender:</label>
        <input type="radio" name="gender" value="male"> Male
        <input type="radio" name="gender" value="female"> Female<br>

        <label>Subscribe:</label>
        <input type="checkbox" name="newsletter"><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>

"""
```

### 5. `Ass4_prog07_scan_host_port_range_to_report.py`

Validates a host + port range and scans with **python-nmap**, writing a report file.

```python
# Write a Python program that accepts a target host and a port range from the user, validates both, scans
# using python-nmap and writes the report (host, port, state, service) to a file.

import nmap
import socket

# Get and validate the host
host = input("Enter target host (IP or name): ")
try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Invalid host")
    exit()

port_range = input("Enter port range (e.g. 20-80): ")
try:
    start, end = port_range.split("-")
    start, end = int(start), int(end)
    if not (1 <= start <= end <= 65535):
        raise ValueError
except ValueError:
    print("Invalid port range. Use format start-end, values 1-65535")
    exit()

# Scan
scanner = nmap.PortScanner()
print("Scanning", ip, "...")
scanner.scan(ip, f"{start}-{end}")

# Write report
with open("scan_report.txt", "w") as f:
    f.write("Host\tPort\tState\tService\n")
    for h in scanner.all_hosts():
        for port in scanner[h]["tcp"]:
            state = scanner[h]["tcp"][port]["state"]
            service = scanner[h]["tcp"][port]["name"]
            line = f"{h}\t{port}\t{state}\t{service}"
            print(line)
            f.write(line + "\n")

print("Report saved to scan_report.txt")
```

### 6. `Ass4_prog08_scan_localhost_tcp_syn_ports.py`

Sends TCP **SYN** packets to ports 20–30 of localhost with Scapy and reports open ports. *(Needs admin/root.)*

```python
# Write a Python program using Scapy to send a TCP SYN packet to ports 20-30 of 127.0.0.1 and report which ports
# are open (SYN-ACK received).
from scapy.all import IP, TCP, sr1, send

target = "127.0.0.1"

for port in range(20, 31):
    # Send SYN packet
    packet = IP(dst=target) / TCP(dport=port, flags="S")
    reply = sr1(packet, timeout=1, verbose=0)

    if reply is None:
        print(f"Port {port}: No response (filtered)")
    elif reply.haslayer(TCP) and reply[TCP].flags == 0x12:
        # 0x12 = SYN-ACK
        print(f"Port {port}: OPEN")
        # Send RST to close the half-open connection
        send(IP(dst=target) / TCP(dport=port, flags="R"), verbose=0)
    else:
        print(f"Port {port}: Closed")

"""
To run this script, open another terminal and start python server listen on port no. 25
python -m http.server 25

"""
```

---

## Assignment 5 — Hashing & Cryptography

### 1. `Ass5_prog01_string_hashes_md5_sha1_sha256.py`

Prints the MD5, SHA-1 and SHA-256 hashes of a string with `hashlib`.

```python
"""
Need to install
pip install cryptography
"""

# Write a Python program to accept a string and display its MD5, SHA-1 and SHA-256 hash values using hashlib.

import hashlib

text = input("Enter a string: ")

# Hash functions work on bytes, so encode the string first
data = text.encode()

print("MD5    :", hashlib.md5(data).hexdigest())
print("SHA-1  :", hashlib.sha1(data).hexdigest())
print("SHA-256:", hashlib.sha256(data).hexdigest())
```

### 2. `Ass5_prog02_fernet_message_encryption_decryption.py`

Encrypts and decrypts a message with **Fernet** (symmetric encryption).

```python
# Write a Python program using the cryptography library (Fernet) to encrypt a message and then decrypt it.

from cryptography.fernet import Fernet

# Generate a secret key
key = Fernet.generate_key()
fernet = Fernet(key)

message = input("Enter a message: ")

# Encrypt (needs bytes)
encrypted = fernet.encrypt(message.encode())
print("Encrypted:", encrypted)

# Decrypt
decrypted = fernet.decrypt(encrypted).decode()
print("Decrypted:", decrypted)
```

### 3. `Ass5_prog03_store_salted_password_hash.py`

Generates a random salt and stores a password as a **PBKDF2-HMAC-SHA256** hash.

```python
# Write a Python program to generate a random salt and store a password as a salted PBKDF2 hash.

import hashlib
import os

password = input("Enter a password to store: ")

# Random 16-byte salt
salt = os.urandom(16)

# PBKDF2 with SHA-256 and 100000 iterations
hash_value = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)

# Save salt and hash as hex text
with open("password_store.txt", "w") as f:
    f.write(salt.hex() + "\n")
    f.write(hash_value.hex() + "\n")

print("Salt :", salt.hex())
print("Hash :", hash_value.hex())
print("Saved to password_store.txt")
```

### 4. `Ass5_prog04_verify_salted_password_hash.py`

Verifies a password against the stored salt + hash. *(Run `Ass5_prog03` first.)*

```python
# Write a Python program to verify a password entered by the user against the stored salted hash.


import hashlib

# Read the stored salt and hash
with open("password_store.txt", "r") as f:
    salt = bytes.fromhex(f.readline().strip())
    stored_hash = bytes.fromhex(f.readline().strip())

password = input("Enter your password: ")

# Hash the entered password with the SAME salt and settings
new_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)

if new_hash == stored_hash:
    print("Password is correct")
else:
    print("Wrong password")
```

### 5. `Ass5_prog06_fernet_file_encryption_decryption.py`

Encrypts/decrypts a file with Fernet and shows that a wrong key fails to decrypt.

```python
# Write a Python program to encrypt the contents of a text file using Fernet and save the key and the encrypted file
# separately. Write another program to decrypt the file. Show that decryption fails with a wrong key.

"""
pip install cryptography twisted
"""

# encrypt_file.py
from cryptography.fernet import Fernet

filename = input("Enter text file name: ")

# Generate a key and save it separately
key = Fernet.generate_key()
with open("secret.key", "wb") as f:
    f.write(key)

# Read, encrypt and save the encrypted file
with open(filename, "rb") as f:
    data = f.read()

encrypted = Fernet(key).encrypt(data)

with open(filename + ".enc", "wb") as f:
    f.write(encrypted)

print("Encrypted file:", filename + ".enc")
print("Key saved in : secret.key")

# ----------------------------------------------------------------------------
# decrypt_file.py

from cryptography.fernet import Fernet, InvalidToken

enc_file = input("Enter encrypted file name: ")
key_file = input("Enter key file name: ")

with open(key_file, "rb") as f:
    key = f.read()
with open(enc_file, "rb") as f:
    encrypted = f.read()

try:
    decrypted = Fernet(key).decrypt(encrypted)
    print("Decryption successful. Contents:")
    print(decrypted.decode())
except InvalidToken:
    print("Decryption FAILED: wrong key or file was changed")

# ----------------------------------------------------------------------------------

# wrong_key.py

from cryptography.fernet import Fernet

with open("wrong.key", "wb") as f:
    f.write(Fernet.generate_key())
print("wrong.key created")


"""
Run this program using following steps:
Create test.txt with some text.
Run encrypt_file.py and enter test.txt.
Run decrypt_file.py with test.txt.enc and secret.key. It shows the text.
Run make_wrong_key.py, then run decrypt_file.py with test.txt.enc and wrong.key. It prints “Decryption FAILED”.
"""
```

---
