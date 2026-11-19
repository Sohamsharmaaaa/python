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
