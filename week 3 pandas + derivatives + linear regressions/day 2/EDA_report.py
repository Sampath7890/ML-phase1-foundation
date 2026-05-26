"""P8 Hard
Full EDA report
Write a function titanic_report(df) that prints a complete report:
→ Total passengers and columns
→ Missing values per column
→ Survival count and rate (%)
→ Survival rate by gender
→ Survival rate by class
→ Average age of survivors vs non-survivors

Call the function. This is a real data science EDA report."""
import pandas as pd
df = pd.read_csv(r'C:\ML phase 1\week 3 pandas + derivatives + linear regressions\day 1/tested.csv')

def titanic_report(df):
    print("=========Titanic Report=========00")

    print("dataset shape :")
    print("Total Passengers: ",df.shape[0])
    print("columns" , df.shape[1],"\n")

    print("Missing values per column")
    print(df.isnull().sum(),"\n")

    print("Survival count and rate (%):")
    survived = df["Survived"].sum()
    not_survived = len(df) - survived
    survival_rate = (survived/len(df))*100

    print("survived :" , survived)
    print("not survived :" , not_survived)
    print("survival rate :" , survival_rate,"\n")

    print("Survival rate by gender: ")
    print(df.groupby("Sex")["Survived"].mean() *100 ,"\n")

    print("Survival rate by class: ")
    print(df.groupby("Pclass")["Survived"].mean() * 100, "\n")

    print("Average age of survivors vs non-survivors:")
    survivor_age = df[df["Survived"] == 1]["Age"].mean()
    non_survivor_age = df[df["Survived"] == 0]["Age"].mean()

    print("Average age of survival age :", survivor_age)
    print("Average age of non-survival age :", non_survivor_age)


titanic_report(df)