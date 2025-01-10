import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

print(df.head())

x = df[["Weight","Volume"]]
y = df[["CO2"]]


regr = linear_model.LinearRegression()
regr.fit(x, y)

predict_co2 = regr.predict([[2300, 1300]])
print(predict_co2)
print(regr.coef_)


###### try put non numeric data to x ######

# Use One-Hot Encoding if the Car column represents nominal categories (no intrinsic order).
# Use Label Encoding if the Car column represents ordinal categories (e.g., "Basic", "Premium", "Luxury").

# Using 1 hot encoding

# Using Label Encoding
from sklearn.preprocessing import LabelEncoder

# Label encode the 'Car' column
le = LabelEncoder()
df = pandas.read_csv("data.csv")
df["Car"] = le.fit_transform(df["Car"])

print(df.head())

# Select features and target
x = df[["Weight", "Volume", "Car"]]
y = df[["CO2"]]

# Fit linear regression model
regr = linear_model.LinearRegression()
regr.fit(x, y)

# Predict CO2
predict_co2 = regr.predict([[2300, 1300, 1]])  # Replace '1' with the appropriate label-encoded value for 'Car'
print("Predicted CO2:", predict_co2)
print("Coefficients:", regr.coef_)