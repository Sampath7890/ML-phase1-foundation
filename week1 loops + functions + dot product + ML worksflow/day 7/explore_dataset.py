from sklearn.datasets import load_iris
iris = load_iris()


print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("Data shape:", iris.data.shape)
print("Target shape:", iris.target.shape)

X = iris.data
y = iris.target

print(X[0])
print(y[0])

print("\n--- First 5 flowers ---")

for i in range(5):
    flower_name = iris.target_names[y[i]]
    print(f"Flower {i+1}: {list(X[i])} -> {flower_name}")

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target column
df["target"] = iris.target

print(df)