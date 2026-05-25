from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# STEP 1: Collect / Load data
iris = load_iris()
X = iris.data
y = iris.target
print("Shape:", X.shape, "| Features:", iris.feature_names)

# STEP 2: Explore it
print("\nFirst 5 rows:\n", X[:5])
print("Class distribution:", np.bincount(y))
# What does each class (0,1,2) represent?

# STEP 3: Choose a model (already chosen: LogisticRegression)

# STEP 4: Train it
X_train, X_test, y_train, y_test = ...  # 80/20 split, random_state=42
model = LogisticRegression(max_iter=200)
model.fit(...)

# STEP 5: Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {acc:.2%}")