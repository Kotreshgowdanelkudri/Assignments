# 24/03/26
# Word Importance TF-IDF

from sklearn.feature_extraction.text import TfidfVectorizer
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# Step 1: Load documents
with open(os.path.join(BASE_DIR, 'datasets', 'documents.txt'), 'r') as f:
    documents = [doc.strip() for doc in f.read().split('\n\n') if doc.strip()]

# Document topic labels for better output
doc_topics = ['Technology', 'Sports', 'Food', 'Travel', 'Science']

# Step 2: Get user input
print("Available documents: 0-Technology, 1-Sports, 2-Food, 3-Travel, 4-Science")
index = int(input("Enter document index (0-4): "))

if index < 0 or index >= len(documents):
    print(f"Error: index must be between 0 and {len(documents) - 1}")
else:
    # Step 3: Apply TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()

    # Get top 5 words for selected document
    doc_vector = tfidf_matrix[index].toarray()[0]
    top_indices = doc_vector.argsort()[-5:][::-1]
    top_words = [feature_names[i] for i in top_indices]
    top_scores = [f"{feature_names[i]} ({doc_vector[i]:.3f})" for i in top_indices]

    # Step 4: Output the results
    topic = doc_topics[index] if index < len(doc_topics) else f"Document {index}"
    print("Input:", f"Document {index} ({topic})")
    print("Processed Data:", f"Document preview: '{documents[index][:80]}...'")
    print("Result:", f"Top keywords: {', '.join(top_words)}")
    print("Explanation:", "TF-IDF scores words by how often they appear in this document vs all documents — higher score = more important/unique word.")