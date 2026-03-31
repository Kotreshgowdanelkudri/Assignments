# 30/03/26
# Prompt Engineering

# Step 1: Get user input
topic = input("Enter topic: ")

# Step 2: Generate prompts
weak = f"Tell me about {topic}."
strong = f"Explain {topic} in detail, including key concepts, examples, and current trends. Provide a structured response with sections."

# Step 3: Output the results
print("Input:", topic)
print("Processed Data:", "Prompts generated")
print("Result:", f"Weak: {weak}\nStrong: {strong}")
print("Explanation:", "Strong prompts are specific and structured to elicit better AI responses.")