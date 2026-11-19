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
