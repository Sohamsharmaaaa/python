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
