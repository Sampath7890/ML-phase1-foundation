import pandas as pd
df = pd.read_csv("../../week 4 Visualization + Probability + Linear Regression Code/day 6/tested.csv")
adults = df[df["Age"] >= 18]
print(adults.to_string() ,"\n", len(adults))
suriviors = df[df["Survived"] == 1]
print(suriviors.to_string() ,"\n" ,len(suriviors))
female = df[df["Sex"] == "female"]
print(female.to_string() ,"\n" ,len(female))
male = df[df["Sex"] == "male"]
print(male.to_string() ,"\n" ,len(male))