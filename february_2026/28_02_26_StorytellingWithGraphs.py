# 28/02/26
# Storytelling With Graphs

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend (no display needed)
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# Step 1: Get user input for dataset
print("Select dataset:")
print("1. house_price_data.csv")
print("2. mall_customers.csv")
choice = input("Enter choice (1 or 2): ").strip()

if choice == '1':
    dataset_name = 'house_price_data.csv'
elif choice == '2':
    dataset_name = 'mall_customers.csv'
else:
    # Allow exact filename input if they prefer
    dataset_name = choice

dataset_path = os.path.join(BASE_DIR, dataset_name)

try:
    df = pd.read_csv(dataset_path)
    columns = list(df.columns)
    
    # Step 2: Show available columns with numbers
    print(f"\nAvailable columns in {dataset_name}:")
    for i, col in enumerate(columns, 1):
        print(f"{i}. {col}")
    
    print("\nPlease enter the NUMBER or the NAME of the column you want.")
    x_input = input("Enter x variable index or name (e.g., 1 or 'age'): ").strip()
    y_input = input("Enter y variable index or name (e.g., 2 or 'annual_income'): ").strip()
    
    # Helper to resolve selection
    def get_column_name(user_input):
        if user_input.isdigit():
            idx = int(user_input) - 1
            if 0 <= idx < len(columns):
                return columns[idx]
        if user_input in columns:
            return user_input
        return None

    x_var = get_column_name(x_input)
    y_var = get_column_name(y_input)
    
    if not x_var or not y_var:
        print(f"\nError: Invalid input. You entered '{x_input}' and '{y_input}', but the program expects a column name (like 'age') or its number from the list above.")
    else:
        plt.scatter(df[x_var], df[y_var])
        plt.xlabel(x_var)
        plt.ylabel(y_var)
        plt.title(f"{x_var} vs {y_var}")
        # Save output in current directory
        plt.savefig('temp_plot.png')  
        plt.close()
        
        # Step 3: Output results
        print("\nInput:", f"Dataset: {dataset_name}, X: {x_var}, Y: {y_var}")
        print("Processed Data:", "Plot generated")
        print("Result:", "Graph saved as temp_plot.png")
        print("Explanation:", "The program creates a scatter plot to visualize the relationship between selected variables.")
        
except FileNotFoundError:
    print(f"Error: dataset '{dataset_name}' not found. Please select a valid option.")