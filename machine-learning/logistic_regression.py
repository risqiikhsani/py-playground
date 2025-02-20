import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Create DataFrame
data = {
    "Age": [36, 42, 23, 52, 43, 44, 66, 35, 52, 35, 24, 18, 45],
    "Experience": [10, 12, 4, 4, 21, 14, 3, 14, 13, 5, 3, 3, 9],
    "Rank": [9, 4, 6, 4, 8, 5, 7, 9, 7, 9, 5, 7, 9],
    "Nationality": ["UK", "USA", "N", "USA", "USA", "UK", "N", "UK", "N", "N", "USA", "UK", "UK"],
    "Go": ["NO", "NO", "NO", "NO", "YES", "NO", "YES", "YES", "YES", "YES", "NO", "YES", "YES"]
}

# df = pd.DataFrame(data)

df = pd.read_csv("data_person.csv")

# Encode categorical variables (Nationality)
df["Nationality"] = LabelEncoder().fit_transform(df["Nationality"])

# Encode target variable (Go: NO → 0, YES → 1)
df["Go"] = df["Go"].map({"NO": 0, "YES": 1})

print(df)

# Features and Target
X = df.drop(columns=["Go"])  # Independent variables
y = df["Go"]  # Target variable

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Display Results
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", report)

# Predict for new data (example)
new_data = np.array([[40, 10, 6, 1]])  # Example input
predicted = model.predict(new_data)
print(f"Prediction for new data: {'YES' if predicted[0] == 1 else 'NO'}")
