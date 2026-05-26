"""P6 Medium
GroupBy analysis
Answer using groupby — one line each:
→ Average age by survival status (survived vs not)
→ Survival rate by gender (% who survived per gender)
→ Average fare by passenger class
→ Number of passengers per class
Write one sentence interpreting each result."""

import pandas as pd
df = pd.read_csv(r'C:\ML phase 1\week 3 pandas + derivatives + linear regressions\day 1/tested.csv')
print("Average age by survival status (survived vs not)")
print(df.groupby('Survived')["Age"].mean())

print("Survival rate by gender (% who survived per gender)")
print(df.groupby('Sex')["Survived"].mean()*100)

print("Average fare by passenger class")
print(df.groupby('Pclass')["Fare"].mean())

print("Number of passengers per class")
print(df.groupby('Pclass')["PassengerId"].count())