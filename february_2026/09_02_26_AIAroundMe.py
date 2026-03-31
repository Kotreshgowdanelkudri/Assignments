# 09/02/26
# AI Around Me

# Step 1: Get user input for scenario selection
print("Select a scenario to see AI applications:")
print("1. Home")
print("2. Work")
print("3. Travel")
choice = input("Enter your choice (1-3): ")

# Step 2: Define AI applications based on choice
if choice == '1':
    scenario = "Home"
    applications = "Smart home devices like Alexa for voice control, AI-powered refrigerators for inventory management, and security cameras with facial recognition."
elif choice == '2':
    scenario = "Work"
    applications = "AI assistants for scheduling, automated data analysis tools, and chatbots for customer service."
elif choice == '3':
    scenario = "Travel"
    applications = "Navigation apps with real-time traffic, AI recommendation systems for hotels, and translation apps for languages."
else:
    scenario = "Invalid choice"
    applications = "Please select a valid option."

# Step 3: Output the results
print("Input:", choice)
print("Processed Data:", f"Selected scenario: {scenario}")
print("Result:", applications)
print("Explanation:", "AI is integrated into daily life to make tasks easier and more efficient in various scenarios.")