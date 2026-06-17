import pandas as pd
df = pd.read_csv('../../week 4 Visualization + Probability + Linear Regression Code/day 6/tested.csv')
print(df.head(5).to_string())
print("\ndataframe shape :",df.shape)
print(df.columns)
print(df.info())
print(df.describe().to_string())