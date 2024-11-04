### Mini Project: **Password Strength Checker

"""

**Goal**:  
Create a program that takes a user's input for a password and checks its strength based on the following criteria:
- At least 8 characters long.
- Contains both uppercase and lowercase letters.
- Includes at least one numeric digit.
- Contains at least one special character (e.g., `!`, `@`, `#`, etc.).

**Steps**:
1. Take the password as input from the user.
2. Use string methods like `.lower()`, `.isupper()`, `.isdigit()`, and slicing to validate the password.
3. Print whether the password is weak, medium, or strong based on how many criteria it satisfies"""

# Take the password as input from the user.

password = input("Please enter your password: ")

# Criteria flags
length_criteria = len(password) >= 8
upper_criteria = any(char.isupper() for char in password)
lower_criteria = any(char.islower() for char in password)
digit_criteria = any(char.isdigit() for char in password)
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/~`"
special_criteria = any(char in special_characters for char in password)

# Count the number of criteria met
criteria_met = sum([length_criteria,upper_criteria,lower_criteria,digit_criteria,special_criteria])

# Determine strength based on criteria met

if criteria_met == 5:
    strength = "strong"
elif criteria_met >= 3:
    strength = "medium"
else:
    strength = "weak"

print(f"Your password is {strength}")
