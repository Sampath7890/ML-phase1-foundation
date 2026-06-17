import pandas as pd
df = pd.read_csv('../../week 4 Visualization + Probability + Linear Regression Code/day 6/tested.csv')
print(df["Age"].head())
print(df[["Name", "Age", "Survived"]].head())
print(df.iloc[0])
print(df.iloc[1:5].to_string())
print(df.iloc[-1])