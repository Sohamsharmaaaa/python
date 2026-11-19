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
