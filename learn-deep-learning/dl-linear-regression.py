# Importing required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

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

# Feature scaling (important for neural networks)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Defining the neural network model
model = Sequential([
    Dense(64, input_dim=X_train.shape[1], activation='relu'),  # Hidden layer 1
    Dense(32, activation='relu'),  # Hidden layer 2
    Dense(1, activation='linear')  # Output layer
])

# Compiling the model
model.compile(optimizer=Adam(learning_rate=0.01), loss='mse', metrics=['mae'])

# Training the model
model.fit(X_train, y_train, epochs=100, batch_size=2, verbose=1)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
print("Neural Network - Mean Squared Error:", mse)
print("Predictions:", y_pred.flatten())
