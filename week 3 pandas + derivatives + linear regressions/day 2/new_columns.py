"""P7 Hard
Create new columns
Add a new column "AgeGroup":
→ Age below 18 → "Child"
→ 18 to 60 → "Adult"
→ Above 60 → "Senior"
Use df["AgeGroup"] = df["Age"].apply(lambda x: ...)
Then: print survival rate per age group using groupby.
Hint: use apply() with a lambda function that uses if/elif/else"""
import pandas as pd
df = pd.read_csv(r'C:\ML phase 1\week 3 pandas + derivatives + linear regressions\day 1/tested.csv')
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["age_group"] = df["Age"].apply(
    lambda x: "child" if x < 18
    else "abult" if x > 60
    else "senior"
)
print(df[["Age" ,"age_group"]].head())

print("survival rate per age group")
print(df.groupby("age_group")["Survived"].mean()*100)