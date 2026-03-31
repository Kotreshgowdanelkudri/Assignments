# 10/03/26
# Spam Classifier Design

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# Step 1: Load data
df = pd.read_csv(os.path.join(BASE_DIR, 'spam_messages.csv'))

# Step 2: Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['message'])
y = df['label']
model = MultinomialNB()
model.fit(X, y)

# Step 3: Get user input
message = input("Enter a message: ")

# Predict
X_new = vectorizer.transform([message])
prediction = model.predict(X_new)[0]
probability = model.predict_proba(X_new)[0]
spam_prob = probability[list(model.classes_).index('spam')] * 100

# Step 4: Output the results
print("Input:", message)
print("Processed Data:", f"Spam probability: {spam_prob:.1f}% | Ham probability: {100 - spam_prob:.1f}%")
print("Result:", f"Classification: {prediction.upper()}")
print("Explanation:", "Naive Bayes classifier predicts if a message is spam or ham based on word frequency patterns.")