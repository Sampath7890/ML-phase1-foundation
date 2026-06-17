import pandas as pd
df = pd.read_csv("../../week 4 Visualization + Probability + Linear Regression Code/day 6/tested.csv")
# Value counts — how many of each category
print(df["Survived"].value_counts())
print(df["Sex"].value_counts())

# GroupBy — average age by survival
print(df.groupby("Survived")["Age"].mean())

# Survival rate by gender
print(df.groupby("Sex")["Survived"].mean())