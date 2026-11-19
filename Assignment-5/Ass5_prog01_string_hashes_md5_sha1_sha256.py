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