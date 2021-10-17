import numpy as np
import vaex
import pandas as pd


df = vaex.open('./companies-on-linkedin.csv.hdf5')
print("info inicial")
print(df.info())
df["Total_employee_estimate"] = df["Total employee estimate"].astype('int')
df["Country_Only"] = df["Country"]
df["Current_employee_estimate"] = df["Current employee estimate"].astype('int')
df["Year_founded"] = df["Year founded"].astype('int')
df['lower_range'] = df["Size range"].str.slice(start=0, stop=1)
df['Company_name'] = df['Company name']
df['Company_URL_Domain'] = df['Company URL domain']
df['upper_range'] = df["Size range"].str.slice(start=4, stop=6)
print("info alinhado")

print(df.describe())
print(df.head(2))

dfArray = df.to_numpy()
print(dfArray)

#df = pd.DataFrame(np_array, columns=[‘Column1’, ‘Column2’])




