import sys
from SPARQLWrapper import SPARQLWrapper, JSON

#os allow us to manipulate dir, folders, files
import os
import os.path

from datetime import datetime

import json
import pandas as pd
from pandas.io.json import json_normalize

filename = 'tablehdf.h5'



nowRaw = datetime.now()
now = str(nowRaw)


store = pd.HDFStore("tablehdfWikipedia.h5")
save_path = './'
name_of_file = now +"StatPreview" ".txt"
completeName = os.path.join(save_path, name_of_file )
f = open(completeName, "w")

#TODO Elaborar página de log
f.write("Log será adicionado futuramente")
f.write('\n\n\n\n')
f.write('-------------------------------------------------------------------------------------------\n')
 
f.close()
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
localHdfsDic = []
for row in df.itertuples():
    localHdfsDic.append({row.id: {
      "latitude" : row.latitude,
      "longitude" : row.longitude,
      "coordinate" : row.coordinate
    }})
  
hdfsWikipediaLocal = localHdfsDic
#print("número de locais: " + str(len(localHdfsDic)))
#df.info()
#print(df.sample(1))