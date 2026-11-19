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
