# 27/03/26
# Semantic Similarity

# Download NLTK data silently if not already present
import nltk
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
from nltk.corpus import wordnet as wn

# Step 1: Get user input
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

# Step 2: Calculate similarity
syn1 = wn.synsets(word1)[0] if wn.synsets(word1) else None
syn2 = wn.synsets(word2)[0] if wn.synsets(word2) else None

if syn1 and syn2:
    similarity = syn1.path_similarity(syn2)
    if similarity is None:
        result = "Similarity could not be computed (words may be in different branches)"
    else:
        result = f"Similarity score: {similarity:.2f} out of 1.0"
    synset_info = f"{syn1.name()} ({syn1.definition()[:40]}...) | {syn2.name()} ({syn2.definition()[:40]}...)"
else:
    result = "One or both words not found in WordNet"
    synset_info = f"word1 found: {syn1 is not None}, word2 found: {syn2 is not None}"

# Step 3: Output the results
print("Input:", f"Word 1: '{word1}', Word 2: '{word2}'")
print("Processed Data:", f"Synsets matched — {synset_info}")
print("Result:", result)
print("Explanation:", "Semantic similarity measures how closely related two words are in meaning (1.0 = identical, 0.0 = unrelated).")