# 12/03/26
# Decision Tree Play Prediction

from sklearn.tree import DecisionTreeClassifier

# Step 1: Sample data (outlook, temperature, humidity, windy -> play)
data = [
    ['sunny', 'hot', 'high', 'false', 'no'],
    ['sunny', 'hot', 'high', 'true', 'no'],
    ['overcast', 'hot', 'high', 'false', 'yes'],
    ['rainy', 'mild', 'high', 'false', 'yes'],
    ['rainy', 'cool', 'normal', 'false', 'yes'],
    ['rainy', 'cool', 'normal', 'true', 'no'],
    ['overcast', 'cool', 'normal', 'true', 'yes'],
    ['sunny', 'mild', 'high', 'false', 'no'],
    ['sunny', 'cool', 'normal', 'false', 'yes'],
    ['rainy', 'mild', 'normal', 'false', 'yes'],
    ['sunny', 'mild', 'normal', 'true', 'yes'],
    ['overcast', 'mild', 'high', 'true', 'yes'],
    ['overcast', 'hot', 'normal', 'false', 'yes'],
    ['rainy', 'mild', 'high', 'true', 'no']
]

# Encode
outlook_map = {'sunny': 0, 'overcast': 1, 'rainy': 2}
temp_map = {'hot': 0, 'mild': 1, 'cool': 2}
hum_map = {'high': 0, 'normal': 1}
wind_map = {'false': 0, 'true': 1}

X = [[outlook_map[r[0]], temp_map[r[1]], hum_map[r[2]], wind_map[r[3]]] for r in data]
y = [1 if r[4] == 'yes' else 0 for r in data]

# Train
model = DecisionTreeClassifier()
model.fit(X, y)

# Step 2: Get user input
outlook = input("Enter outlook (sunny/overcast/rainy): ")
temp = input("Enter temperature (hot/mild/cool): ")
hum = input("Enter humidity (high/normal): ")
wind = input("Enter windy (false/true): ")

# Encode input
x_new = [outlook_map[outlook], temp_map[temp], hum_map[hum], wind_map[wind]]
prediction = model.predict([x_new])[0]

# Step 3: Output the results
print("Input:", f"Outlook: {outlook}, Temp: {temp}, Hum: {hum}, Wind: {wind}")
print("Processed Data:", f"Encoded: {x_new}")
print("Result:", "Play" if prediction == 1 else "No Play")
print("Explanation:", "Decision tree predicts whether to play based on weather conditions.")