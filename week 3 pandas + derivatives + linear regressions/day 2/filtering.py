"""P4 Medium
Filtering
Create separate DataFrames for:
→ All survivors
→ All children (age below 18)
→ All female survivors
→ All passengers in class 1 who survived
Print the count of each group."""

import pandas as pd
df = pd.read_csv(r'/week 3 pandas + derivatives + linear regressions/day 1/tested.csv')

Survivors = df[df['Survived'] == 1]
Children = df[df['Age']<18]
female_survived = df[(df['Sex']=='female') & (df['Survived']==1)]
Class1_survived = df[(df['Pclass']==1) & (df['Survived']==1)]

print("all survivors :\n",Survivors)
print("all female survivors :\n",female_survived)
print("all premium class survived :\n",Class1_survived)
print("all children :\n",Children)