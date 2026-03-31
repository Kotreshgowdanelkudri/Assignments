# 24/02/26
# Dataset Detective

import pandas as pd
import os

# Resolve base directory relative to this script
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# Step 1: Get user input for dataset selection
print("Select dataset:")
print("1. house_price_data.csv")
print("2. mall_customers.csv")
print("3. spam_messages.csv")
choice = input("Enter choice (1-3): ")

if choice == '1':
    df = pd.read_csv(os.path.join(BASE_DIR, 'house_price_data.csv'))
    stats = df.describe()
    result = "House price stats"
elif choice == '2':
    df = pd.read_csv(os.path.join(BASE_DIR, 'mall_customers.csv'))
    stats = df.describe()
    result = "Mall customers stats"
elif choice == '3':
    df = pd.read_csv(os.path.join(BASE_DIR, 'spam_messages.csv'))
    stats = df['label'].value_counts()
    result = "Spam messages counts"
else:
    stats = "Invalid choice"
    result = "Error"

# Step 2: Output the results
print("Input:", choice)
print("Processed Data:", stats)
print("Result:", result)
print("Explanation:", "The program loads and analyzes the selected dataset to provide statistical insights.")