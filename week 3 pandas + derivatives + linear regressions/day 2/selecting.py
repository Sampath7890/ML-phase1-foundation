"""P2 Easy
Selecting
Print only the Name, Age, Sex and Survived columns.
Print the 10th passenger (row index 9) — all their details.
Print the last 3 passengers using iloc."""

import pandas as pd
df = pd.read_csv(r'/week 4 Visualization + Probability + Linear Regression Code/day 2/tested.csv')
print(df[["Name",  "Age" , "Sex" , "Survived"]].to_string())
print("10th passanger details : \n")
print(df.iloc[9])
print("last 3 passengers using iloc : \n")
print(df.iloc[-3:])
