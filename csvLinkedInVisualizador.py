import pandas as pd

df = pd.read_csv("companies.csv")

localcsvLinkedinDic = []
for row in df.itertuples():
    localcsvLinkedinDic.append({row.ID : {
      "latitude" : row.latitude,
      "longitude" : row.longitude,
    }})
  
csvLinkedinLocais = localcsvLinkedinDic
#print("número de locais: " + str(len(localcsvLinkedinDic)))
#print(df.sample(1))