# 02/03/26
# ML Idea Generator

# Step 1: Get user input for domain
domain = input("Enter domain (health/finance/education): ").strip().lower()

# Step 2: Generate idea based on domain
if domain == 'health':
    idea = "Predict patient readmission using historical data."
elif domain == 'finance':
    idea = "Detect fraudulent transactions with anomaly detection."
elif domain == 'education':
    idea = "Personalize learning paths based on student performance."
else:
    idea = "Invalid domain selected."

# Step 3: Output the results
print("Input:", domain)
print("Processed Data:", "Idea generated")
print("Result:", idea)
print("Explanation:", "Machine learning ideas are tailored to specific domains to solve real-world problems.")