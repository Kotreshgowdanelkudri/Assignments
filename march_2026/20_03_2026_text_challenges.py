# 20/03/26
# Text Challenges

# Step 1: Get user input
sentence = input("Enter a sentence: ")

# Step 2: Process
word_count = len(sentence.split())
char_count = len(sentence)
upper_count = sum(1 for c in sentence if c.isupper())

# Step 3: Output the results
print("Input:", sentence)
print("Processed Data:", f"Words: {word_count}, Chars: {char_count}, Upper: {upper_count}")
print("Result:", "Text analyzed")
print("Explanation:", "The program counts words, characters, and uppercase letters in the input sentence.")