# 17/02/26
# Logic Builder

# Step 1: Get user inputs for boolean values
a = input("Enter first boolean (True/False): ").strip().lower() == 'true'
b = input("Enter second boolean (True/False): ").strip().lower() == 'true'

# Step 2: Build logic operations
and_result = a and b
or_result = a or b
not_a = not a
not_b = not b

# Step 3: Output the results
print("Input:", f"A: {a}, B: {b}")
print("Processed Data:", f"AND: {and_result}, OR: {or_result}, NOT A: {not_a}, NOT B: {not_b}")
print("Result:", f"Logic operations completed")
print("Explanation:", "Boolean logic operations combine inputs to produce true or false results.")