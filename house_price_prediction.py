import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("house_prices.csv")

print("=== House Price Dataset ===")
print(df)

# Features and target
X = df[["Area"]]
y = df["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# User input
area = float(input("Enter House Area (sq ft): "))

# Prediction
predicted_price = model.predict([[area]])

print(f"\nPredicted House Price: ₹{predicted_price[0]:,.2f}")

# Graph
plt.scatter(df["Area"], df["Price"])
plt.plot(df["Area"], model.predict(X))
plt.title("House Price Prediction")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.show()