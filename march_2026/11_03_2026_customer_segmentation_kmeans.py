# 11/03/26
# Customer Segmentation K-Means

import pandas as pd
from sklearn.cluster import KMeans
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# Step 1: Load data
df = pd.read_csv(os.path.join(BASE_DIR, 'mall_customers.csv'))

# Step 2: Train K-Means on the feature columns
features = df[['age', 'annual_income', 'spending_score']]
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
kmeans.fit(features)
df['cluster'] = kmeans.labels_

# Step 3: Get user input
age = int(input("Enter age: "))
income = int(input("Enter annual income: "))
spending = int(input("Enter spending score (1-100): "))

# Predict cluster - use DataFrame to match training feature names
X_new = pd.DataFrame([[age, income, spending]],
                     columns=['age', 'annual_income', 'spending_score'])
cluster = kmeans.predict(X_new)[0]

# Show brief cluster profile
cluster_data = df[df['cluster'] == cluster][['age', 'annual_income', 'spending_score']]
cluster_profile = f"Avg Age: {cluster_data['age'].mean():.1f}, Avg Income: {cluster_data['annual_income'].mean():.0f}, Avg Spending: {cluster_data['spending_score'].mean():.1f}"

# Step 4: Output the results
print("Input:", f"Age: {age}, Income: {income}, Spending Score: {spending}")
print("Processed Data:", f"Cluster {cluster} profile — {cluster_profile}")
print("Result:", f"You belong to Customer Segment {cluster}")
print("Explanation:", "K-Means groups customers into 5 segments based on age, income, and spending patterns.")