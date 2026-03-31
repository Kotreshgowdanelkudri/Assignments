# 12/02/26
# Smart Input Program

# Step 1: Get user input for type and value
input_type = input("Enter input type (number/text): ").strip().lower()
value = input("Enter the value: ")

# Step 2: Process based on type
if input_type == 'number':
    try:
        num = float(value)
        processed = f"Square: {num**2}, Cube: {num**3}"
        result = f"Processed number: {num}"
    except ValueError:
        processed = "Invalid number"
        result = "Error"
elif input_type == 'text':
    processed = f"Length: {len(value)}, Uppercase: {value.upper()}"
    result = f"Processed text: {value}"
else:
    processed = "Unknown type"
    result = "Error"

# Step 3: Output the results
print("Input:", f"Type: {input_type}, Value: {value}")
print("Processed Data:", processed)
print("Result:", result)
print("Explanation:", "The program processes inputs differently based on their type to provide relevant information.")