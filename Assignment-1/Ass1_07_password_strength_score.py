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
