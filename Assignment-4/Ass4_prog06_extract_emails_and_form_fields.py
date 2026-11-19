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
