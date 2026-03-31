# 07/03/26
# KNN Recommendation

import pandas as pd
from sklearn.neighbors import NearestNeighbors
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# Step 1: Load data
df = pd.read_csv(os.path.join(BASE_DIR, 'mall_customers.csv'))

# Step 2: Get user input for preferences
age = int(input("Enter age: "))
income = int(input("Enter annual income: "))
spending = int(input("Enter spending score (1-100): "))

# Step 3: Fit KNN - use DataFrame to match training feature names
knn = NearestNeighbors(n_neighbors=3)
knn.fit(df[['age', 'annual_income', 'spending_score']])

# Find neighbors - wrap in DataFrame to avoid feature name warning
X_query = pd.DataFrame([[age, income, spending]],
                       columns=['age', 'annual_income', 'spending_score'])
distances, indices = knn.kneighbors(X_query)
neighbors = df.iloc[indices[0]]

# Step 4: Output the results
print("Input:", f"Age: {age}, Income: {income}, Spending Score: {spending}")
print("Processed Data:", f"Top 3 similar customers:\n{neighbors[['age', 'annual_income', 'spending_score']].to_string(index=False)}")
print("Result:", "Recommended similar customers found successfully")
print("Explanation:", "KNN finds the 3 customers with the most similar profiles for personalized recommendations.")