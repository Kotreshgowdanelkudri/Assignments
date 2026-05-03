# 03/04/2026
# NLP Mini App - Keyword Extractor

import re
from collections import Counter

def extract_keywords(text, top_n=5):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split into words
    words = text.split()
    
    # Simple stop words list
    stop_words = {'the', 'is', 'in', 'and', 'of', 'to', 'a', 'for', 'on', 'with', 'as', 'it', 'by', 'that', 'this', 'are', 'be', 'or', 'from', 'at'}
    
    # Filter stop words
    keywords = [word for word in words if word not in stop_words]
    
    # Count frequency
    word_counts = Counter(keywords)
    return word_counts.most_common(top_n)

if __name__ == "__main__":
    print("=== Keyword Extractor ===")
    text = input("Enter a text to extract keywords: ")
    
    if text.strip():
        keywords = extract_keywords(text)
        print("\nProcessed Data: Extracted Top Keywords")
        print("Result:")
        for word, count in keywords:
            print(f"- {word}: {count} occurrences")
        print("\nExplanation: A simple keyword extractor that removes basic stop words and counts word frequency.")
    else:
        print("No text provided.")
