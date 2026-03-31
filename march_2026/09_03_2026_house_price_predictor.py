# 09/03/26
# House Price Predictor

import pandas as pd
from sklearn.linear_model import LinearRegression
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# Step 1: Load data
df = pd.read_csv(os.path.join(BASE_DIR, 'house_price_data.csv'))

# Step 2: Train model
X = df[['square_feet', 'bedrooms', 'bathrooms', 'location_score']]
y = df['price']
model = LinearRegression()
model.fit(X, y)

# Step 3: Get user input
sqft = int(input("Enter square feet: "))
beds = int(input("Enter bedrooms: "))
baths = int(input("Enter bathrooms: "))
loc = int(input("Enter location score (1-10): "))

# Predict - use DataFrame to match training feature names (avoids sklearn warning)
X_new = pd.DataFrame([[sqft, beds, baths, loc]],
                     columns=['square_feet', 'bedrooms', 'bathrooms', 'location_score'])
prediction = model.predict(X_new)[0]

# Step 4: Output the results
print("Input:", f"Sqft: {sqft}, Beds: {beds}, Baths: {baths}, Location Score: {loc}")
print("Processed Data:", f"Features — square_feet: {sqft}, bedrooms: {beds}, bathrooms: {baths}, location_score: {loc}")
print("Result:", f"Predicted price: ${prediction:,.2f}")
print("Explanation:", "Linear regression predicts house price based on input features like size, rooms, and location.")