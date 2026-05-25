import pandas as pd

# Load data
df = pd.read_csv("tested.csv")

# 1. Original shape
print("Original shape:", df.shape)

# 2. Missing values BEFORE cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 3. Drop rows with missing values (new dataframe)
df_clean = df.dropna()
print("\nAfter dropna shape:", df_clean.shape)

# 4. Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Optional: Fill Fare too
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# 5. Missing values AFTER fillna
print("\nMissing values after fillna:")
print(df.isnull().sum())

# 6. Final shape of original dataframe
print("\nFinal shape after fillna:", df.shape)