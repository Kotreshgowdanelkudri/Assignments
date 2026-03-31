# 28/03/26
# Break the AI

# Step 1: Get user input
prompt = input("Enter a tricky prompt: ")

# Step 2: Simulate AI response
if "ignore" in prompt.lower():
    response = "I cannot ignore previous instructions."
elif "repeat" in prompt.lower():
    response = "Repeating: " + prompt
else:
    response = "Normal response to: " + prompt

# Step 3: Output the results
print("Input:", prompt)
print("Processed Data:", "Prompt analyzed for tricks")
print("Result:", response)
print("Explanation:", "AI responses are designed to handle tricky prompts safely.")