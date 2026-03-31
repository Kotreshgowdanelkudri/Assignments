# 07/02/26
# Strong Password Authentication

import re

# Step 1: Get user input for password
password = input("Enter a password to check its strength: ")

# Step 2: Perform checks for password strength criteria
length_check = len(password) >= 8
upper_check = bool(re.search(r'[A-Z]', password))
lower_check = bool(re.search(r'[a-z]', password))
digit_check = bool(re.search(r'\d', password))
special_check = bool(re.search(r'[!@#$%^&*()_+{}|:<>?]', password))

# Step 3: Determine if the password is strong
is_strong = length_check and upper_check and lower_check and digit_check and special_check

# Step 4: Output the results
print("Input:", password)
print("Processed Data:", f"Length >=8: {length_check}, Uppercase: {upper_check}, Lowercase: {lower_check}, Digit: {digit_check}, Special: {special_check}")
print("Result:", "Strong" if is_strong else "Weak")
print("Explanation:", "A strong password must be at least 8 characters long and include uppercase letters, lowercase letters, digits, and special characters." if not is_strong else "The password meets all the strength criteria.")