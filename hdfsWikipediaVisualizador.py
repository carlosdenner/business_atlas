import sys
from SPARQLWrapper import SPARQLWrapper, JSON

from sqlalchemy import create_engine
from pandas.io import sql
import re

import plotly.express as px
import plotly.io as pio

import plotly.graph_objects as go

import nominatintest as nm



#os allow us to manipulate dir, folders, files
import os
import os.path

from datetime import datetime

import json
import pandas as pd
from pandas.io.json import json_normalize




nowRaw = datetime.now()
nowStart = str(nowRaw)
print("started at " + nowStart)

print(nowStart)
store = pd.HDFStore("tablehdfWikipedia.h5")
save_path = './'
name_of_file = nowStart +"StatPreview" ".txt"
completeName = os.path.join(save_path, name_of_file )
f = open(completeName, "w")

#TODO Elaborar página de log



df = store.select('/data')

#Here's an row example:
#Pandas(Index=70267, 
#        latitude=42.762939453125, 
#        longitude=11.128694534301758, 
#        company='Latte Maremma', 
#        coordinate='Point(11.128694689 42.762938526)', 
#        inception='1961-02-12T00:00:00Z', 
#        industry=nan, 
#        id='http://www.wikidata.org/entity/Q108375584',
#        id_industry=nan, 
#        id_country='http://www.wikidata.org/entity/Q38', 
#        country=nan)
allsum = 0.0
localHdfsWikipediaDic = []
for row in df.itertuples():
    localHdfsWikipediaDic.append({
      "Id": row.id,
      "latitude" : row.latitude,
      "longitude" : row.longitude,
      "company" : row.company,
      "coordinate" : row.coordinate,
      "inception" : row.industry,
      "id_industry" : row.id_industry,
      "id_country" : row.id_country,
      "country" : row.country 
    })
  
hdfsWikipediaLocal = localHdfsWikipediaDic
print('Df info:')
print('------------------------')
print(df.info())
df2 = df.dropna(subset = ['industry'])
print('Df2 info:')
print('------------------------')
print(df2.info())
print(df2['industry'])
namecount = 0
IDs=[]
for name in df['id']:
    ID_n = name.rsplit('/', 1)[1]
    ID = re.findall('\d+', ID_n)
    #print(ID[0], ID_n)
    IDs.append(ID[0])
    namecount = namecount + 1
print('--------------------->>>>>>>------')
print('numero de nomes é ' + str(namecount))
df ['ID'] = IDs
print (df['ID'].describe())
df['ID']= df['ID'].astype(int)

df.rename(columns={'id':'URL'}, inplace=True)
df['company_foundation'] = df['inception'].str.extract(r'(\d{4})')
pd.to_numeric(df['company_foundation'])
df = df.set_index(['ID'])
df["latitudestr"] = df["latitude"].apply(str)
df["longitudestr"] = df["longitude"].apply(str)
print("====================chegou aqui==================")
df["CountryName"] = nm.location(df["latitudestr"], df["longitudestr"])

df.to_csv("./wikiwithcountry.csv")

industries = df.dropna(subset=['latitude'])
#print(industries)

industries.groupby('latitude')[['company', 'country']].apply(lambda x: x.values.tolist())
print('latitutdes info------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(industries.info())

industries = pd.DataFrame(industries)
industriescsv = industries.to_csv('./industries.csv')


IDs=[]
#for name in industries['id_industry']:
   # ID_n = name.rsplit('/', 1)[1]
  #  ID = re.findall('\d+', ID_n)
#    print(ID, ID_n)
 #   IDs.append(ID[0])
    
#industries ['ID_industry'] = IDs
#industries['ID_industry']= industries['ID_industry'].astype(int)
#industries.set_index([industries.index, 'ID_industry'], inplace=True)
industries['id_wikipedia']=industries['id_industry']
industries.drop('id_industry', axis=1, inplace=True)  

industries = pd.DataFrame(industries)
print(industries.info())
print(industries.sample(3))

nowRaw = datetime.now()
nowEnd = str(nowRaw)
print("ended at " + nowEnd)
#print("número de locais: " + str(len(localHdfsDic)))


#someString = df.head(1).astype(str).values.flatten().tolist()
def listToString(listToString): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in listToString: 
        str1 += ele  + "||"
    
    # return string  
    return str1 

save_path = './'
name_of_file = nowStart + "hdfsWikipedia"+ "StatPreview" ".txt"
completeName = os.path.join(save_path, name_of_file )
f = open(completeName, "w")

f.write("Log será adicionado futuramente\n")

f.write('\n\n\n\n')
f.write('-------------------------------------------------------------------------------------------\n')
 
f.close()
