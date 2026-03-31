# 26/03/26
# Movie Review Sentiment

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# Step 1: Load reviews
with open(os.path.join(BASE_DIR, 'datasets', 'movie_reviews.txt'), 'r') as f:
    reviews = f.readlines()

# Labels match movie_reviews.txt content:
# Line 1: positive, Line 2: negative, Line 3: positive, Line 4: negative, Line 5: positive
labels = ['positive', 'negative', 'positive', 'negative', 'positive']

# Step 2: Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)
y = labels
model = MultinomialNB()
model.fit(X, y)

# Step 3: Get user input
review = input("Enter a movie review: ")

# Predict
X_new = vectorizer.transform([review])
prediction = model.predict(X_new)[0]
probability = model.predict_proba(X_new)[0]
pos_prob = probability[list(model.classes_).index('positive')] * 100

# Step 4: Output the results
print("Input:", review)
print("Processed Data:", f"Positive probability: {pos_prob:.1f}% | Negative probability: {100 - pos_prob:.1f}%")
print("Result:", f"Sentiment: {prediction.upper()}")
print("Explanation:", "Naive Bayes classifies movie review sentiment as positive or negative based on word patterns.")