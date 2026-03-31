# 19/02/26
# Student Data Manager

# Note: Data does not persist between runs (in-memory only)
students = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}  # Pre-populated with sample data

# Step 1: Get user action
action = input("Enter action (add/search): ").strip().lower()

if action == 'add':
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    students[name] = grade
    processed = f"Added {name} with grade {grade}"
    result = "Student added"
elif action == 'search':
    name = input("Enter student name to search: ")
    if name in students:
        processed = f"Found {name}: {students[name]}"
        result = students[name]
    else:
        processed = f"{name} not found"
        result = "Not found"
else:
    processed = "Invalid action"
    result = "Error"

# Step 2: Output the results
print("Input:", f"Action: {action}")
print("Processed Data:", processed)
print("Result:", result)
print("Explanation:", "The program manages student data by allowing addition and searching of records.")