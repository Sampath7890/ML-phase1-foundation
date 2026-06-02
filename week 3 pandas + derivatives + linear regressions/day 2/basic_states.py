"""P3 Easy
Basic stats
Answer using Pandas — one line each:
How many passengers survived?
How many did not survive?
What was the average age of all passengers?
What was the most expensive ticket fare?"""

import pandas as pd
df = pd.read_csv(r'/week 4 Visualization + Probability + Linear Regression Code/day 2/tested.csv')
print("Survived : ",df['Survived'].sum())
print("not survived :",(df['Survived'] == 0).sum())
print("Average aage :",df["Age"].mean())
print("youngest aage :",df["Age"].min())
print("oldest aage :",df["Age"].max())
print("most expensive fare:", df["Fare"].max())
print(df.loc[df['Fare'].idxmax()])