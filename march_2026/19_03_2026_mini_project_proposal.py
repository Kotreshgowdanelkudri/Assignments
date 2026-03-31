# 19/03/26
# Mini Project Proposal

# Step 1: Get user input for topic
topic = input("Enter topic (web app/data analysis/game): ").strip().lower()

# Step 2: Generate proposal
if topic == 'web app':
    proposal = "Build a task management web app using Flask and SQLite."
elif topic == 'data analysis':
    proposal = "Analyze sales data with pandas and visualize with matplotlib."
elif topic == 'game':
    proposal = "Create a simple text-based adventure game in Python."
else:
    proposal = "Invalid topic."

# Step 3: Output the results
print("Input:", topic)
print("Processed Data:", "Proposal generated")
print("Result:", proposal)
print("Explanation:", "The proposal outlines a mini project idea based on the selected topic.")