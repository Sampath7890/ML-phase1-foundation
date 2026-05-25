import pandas as pd
df = pd.read_csv('tested.csv')
print(df.head(5).to_string())
print("\ndataframe shape :",df.shape)
print(df.columns)
print(df.info())
print(df.describe().to_string())