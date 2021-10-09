import vaex
from datetime import datetime


# Reading a HDF5 file
df = vaex.open('output_data_agr.csv')

def city (locality):
        try:
            return str(locality.split(',')[0])
        except:
            return 'None'
def estate (locality):
    try:
        return str(locality.split(',')[1])
    except:
        return 'None'
def country (locality):
    try:
        return str(locality.split(',')[2])
    except:
        return 'None'

nowRaw = datetime.now()
nowStart = str(nowRaw)
print("op começou as " + nowStart)
df['city'] = df["Locality"].apply(city)
df['estate'] = df["Locality"].apply(estate)
df['country'] = df["Locality"].apply(country)
df.export_csv('./city_size_data.csv')
nowRaw = datetime.now()
nowEnd = str(nowRaw)
print("cabou as " + nowEnd)
print(df)
