import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

# First dataset
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Scatter plot of the data
plt.scatter(x, y)
plt.title("Scatter Plot of x vs. y")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Linear regression using scipy.stats
slope, intercept, r, p, std_err = stats.linregress(x, y)

# r value
print(f"Correlation coefficient (r): {r}")
# Interpretation: r close to -1 or 1 means a strong relationship.

# Predict y using the regression line
def myfunc(x):
    return slope * x + intercept

# Predicted values
model = list(map(myfunc, x))

# Scatter plot with regression line
plt.scatter(x, y, label="Data points")
plt.plot(x, model, color="red", label="Regression line")
plt.title("Linear Regression")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Calculate and print R² score
r2 = r2_score(y, model)
print(f"R² Score: {r2}")

# Second dataset (not fit for linear regression)
x = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f"Correlation coefficient for second dataset (r): {r}")

# Linear regression for second dataset
def myfunc2(x):
    return slope * x + intercept

model = list(map(myfunc2, x))

# Scatter plot with regression line for second dataset
plt.scatter(x, y, label="Data points")
plt.plot(x, model, color="red", label="Regression line")
plt.title("Linear Regression (Second Dataset)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

# Calculate and print R² score
r2 = r2_score(y, model)
print(f"R² Score: {r2}")
