import pandas as pd

df = pd.read_csv("companies.csv")
print(df.info())
print(df.sample(5))
#for row in df.itertuples():
#    print(row.text)