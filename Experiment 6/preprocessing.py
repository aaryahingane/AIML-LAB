import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Create dataset
data = {
    "Name": ["Amit", "Riya", "Neha", "Raj", "Sara"],
    "Age": [20, None, 22, 21, 23],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai"],
    "Marks": [80, 90, None, 70, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# -------------------------
# Step 1: Handle Missing Values
# -------------------------
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDataset after filling missing values")
print(df)

# -------------------------
# Step 2: Encoding
# -------------------------
encoder = LabelEncoder()

df["City"] = encoder.fit_transform(df["City"])

print("\nDataset after encoding")
print(df)

# -------------------------
# Step 3: Normalization
# -------------------------
scaler = MinMaxScaler()

df[["Age", "Marks"]] = scaler.fit_transform(df[["Age", "Marks"]])

print("\nDataset after normalization")
print(df)

# Final dataset
print("\nFinal Preprocessed Dataset")
print(df)
