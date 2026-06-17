import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv(r"C:\ML phase 1\week 4 Visualization + Probability + Linear Regression Code\day 6\tested.csv")

# Select features and target
features = ["Pclass", "Age", "SibSp", "Parch"]
target = "Survived"

# Handle missing values in features
df["Age"] = df["Age"].fillna(df["Age"].median())

# Remove rows where target is missing
df = df.dropna(subset=[target])

# Create X and y
X = df[features]
y = df[target]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Evaluation Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("===== MODEL PERFORMANCE =====")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.2f}")

# Coefficients
print("\n===== COEFFICIENTS =====")

for feature, coef in zip(features, model.coef_):
    print(f"{feature}: {coef:.4f}")

print(f"\nIntercept: {model.intercept_:.4f}")

# Sample Predictions
results = pd.DataFrame({
    "Actual Fare": y_test.values,
    "Predicted Fare": y_pred
})

print("\n===== SAMPLE PREDICTIONS =====")
print(results.head(10))