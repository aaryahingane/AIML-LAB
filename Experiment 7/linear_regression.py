import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -------------------------
# Step 1: Load Dataset
# -------------------------
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

columns = [
    "mpg", "cylinders", "displacement", "horsepower",
    "weight", "acceleration", "year", "origin", "name"
]

df = pd.read_csv(url, sep=r"\s+", names=columns, na_values="?")

print("First Five Rows")
print(df.head())

# -------------------------
# Step 2: Select Columns
# -------------------------
df = df[["horsepower", "weight", "mpg"]]

# Remove missing values
df = df.dropna()

print("\nCleaned Dataset")
print(df.head())

# -------------------------
# Step 3: Define X and Y
# -------------------------
X = df[["horsepower", "weight"]]
y = df["mpg"]

# -------------------------
# Step 4: Split Dataset
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))

# -------------------------
# Step 5: Create Model
# -------------------------
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# -------------------------
# Step 6: Make Predictions
# -------------------------
y_pred = model.predict(X_test)

print("\nActual MPG Values:")
print(y_test.head())

print("\nPredicted MPG Values:")
print(y_pred[:5])

# -------------------------
# Step 7: Evaluate Model
# -------------------------
print("\nModel Evaluation")

print("Mean Absolute Error:",
      mean_absolute_error(y_test, y_pred))

print("Mean Squared Error:",
      mean_squared_error(y_test, y_pred))

print("R2 Score:",
      r2_score(y_test, y_pred))

# -------------------------
# Step 8: Display Coefficients
# -------------------------
print("\nModel Coefficients")

print("Horsepower Coefficient:", model.coef_[0])
print("Weight Coefficient:", model.coef_[1])
print("Intercept:", model.intercept_)

# -------------------------
# Step 9: Predict for a New Car
# -------------------------
new_car = pd.DataFrame(
    [[100, 2500]],
    columns=["horsepower", "weight"]
)

new_prediction = model.predict(new_car)

print("\nNew Car Details")
print("Horsepower: 100")
print("Weight: 2500")

print("Predicted Fuel Efficiency:",
      new_prediction[0], "MPG")

# -------------------------
# Step 10: Visualization
# -------------------------
plt.scatter(y_test, y_pred)

plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.title("Actual vs Predicted Fuel Efficiency")

plt.show()
