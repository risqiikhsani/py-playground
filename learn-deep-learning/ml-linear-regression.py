# Importing required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample dataset (features: size, number of rooms, location index; target: price)
data = {
    "Size": [1500, 1700, 2000, 2100, 2500],
    "Rooms": [3, 3, 4, 4, 5],
    "LocationIndex": [1, 2, 2, 3, 3],
    "Price": [300000, 350000, 400000, 450000, 500000]
}
df = pd.DataFrame(data)

# Splitting data into features and target
X = df[["Size", "Rooms", "LocationIndex"]]
y = df["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training using Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print("Linear Regression - Mean Squared Error:", mse)
print("Predictions:", y_pred)
