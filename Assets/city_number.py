#This script opens the linkedin file and generates a view on it showing in csv
#places with their locality down to city
#Generates a view with the following data from the database:
# Locality,Industry,Total_employee_estimate_mean, Total_employee_estimate_std,
# mean_size,max_size,city,estate,country called city_size_data.csv

import vaex
from datetime import datetime


# Reading a HDF5 file
df = vaex.open('../DataSetExtractions/output_data_agr.csv')

#Turning locality into city/state/country
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
#displaying information about the proccess
nowRaw = datetime.now()
nowStart = str(nowRaw)
print("Started at " + nowStart)
df['city'] = df["Locality"].apply(city)
df['estate'] = df["Locality"].apply(estate)
df['country'] = df["Locality"].apply(country)


df.export_csv('../DataSetExtrations/city_size_data.csv')


nowRaw = datetime.now()
nowEnd = str(nowRaw)
print("Ended at " + nowEnd)
print(df)
