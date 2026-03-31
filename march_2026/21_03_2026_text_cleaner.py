# 21/03/26
# Text Cleaner

import re
import string

# Step 1: Get user input
text = input("Enter raw text: ")

# Step 2: Clean text
cleaned = text.lower()
cleaned = re.sub(r'[^\w\s]', '', cleaned)  # Remove punctuation
cleaned = ' '.join(cleaned.split())  # Remove extra spaces

# Step 3: Output the results
print("Input:", text)
print("Processed Data:", f"Lowercased and punctuation removed")
print("Result:", cleaned)
print("Explanation:", "Text is cleaned by converting to lowercase and removing punctuation and extra spaces.")