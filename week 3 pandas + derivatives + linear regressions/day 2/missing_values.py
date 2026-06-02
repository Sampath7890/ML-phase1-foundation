"""P5 Medium
Missing values
How many missing values does Age have?
Fill missing Age values with the median age.
How many missing values does Age have now?
Drop any rows where Embarked is missing.
Print the shape before and after each operation."""
import pandas as pd
df = pd.read_csv(r'/week 4 Visualization + Probability + Linear Regression Code/day 2/tested.csv')
print("original shape: ",df.shape)
print("missing values Before operantions \n",df.isnull().sum())
print("missing values of Age",df['Age'].isnull().sum())
print("Shape before fillna ",df.shape)
df['Age'] = df['Age'].fillna(df['Age'].median())
print("Shape after fillna ",df.shape)
print("\nMissing Age values after fillna:",
      df['Age'].isnull().sum())
print("\nMissing values after operations:")
print(df.isnull().sum())