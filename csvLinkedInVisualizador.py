import pandas as pd

df = pd.read_csv("companies.csv")

localcsvLinkedinDic = []
for row in df.itertuples():
    localcsvLinkedinDic.append({
      "Id": row.ID,
      "latitude" : row.latitude,
      "longitude" : row.longitude,
    })
  
csvLinkedinLocais = localcsvLinkedinDic
print("número de locais: " + str(len(localcsvLinkedinDic)))
print(df.sample(1))

#if((float(listCsv["latitude"]) >= 10.0000) or (float(listCsv["latitude"]) <= -10.0000)):
#        csvlatitudestring = str(listCsv["latitude"]).replace("-", "")
#    else:
#        csvlatitudestring = "0" + str(listCsv["latitude"]).replace("-", "")
#    if((float(listCsv["longitude"]) >= 10.00000000) or (float(listCsv["longitude"]) <= 10.00000000)):
#        csvlongitudestring = listCsv["longitude"].replace("-", "")
#    else:
#        csvlongitudestring = "0" + str(listCsv["longitude"]).replace("-", "")
#    
#   csvlatituderow = csvlatituderow + [csvlatitudestring]
#    csvlongituderow = csvlongituderow + [csvlongitudestring]
#    hdfslatituderow = hdfslatituderow + [listHdfs["latitude"]]
#    hdfslongituderow = hdfslongituderow + [listHdfs["longitude"]]