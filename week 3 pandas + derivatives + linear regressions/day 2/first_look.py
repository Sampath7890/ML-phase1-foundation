"""P1 Easy
First look
Load titanic.csv. Print: total passengers, total columns, column names, data types of each column, how
many missing values in each column."""

import pandas as pd
df = pd.read_csv(r'/week 4 Visualization + Probability + Linear Regression Code/day 2/tested.csv')
print("total passangers :",df.shape[0])
print("total columns :",df.shape[1])
print("column names :", df.columns)
print("data types of each column :",df.dtypes)
print("how many missing values in each column :",df.isnull().sum())
