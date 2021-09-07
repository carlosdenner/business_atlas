import hdfsWikipediaVisualizador
#hdfsWikipediaVisualizador.hdfsWikipediaLocal é um dic com as localizações do hdfs

#da wikipedia num dictionary de elementos ID = {"latitude": latitudeID, "longitude" : longitudeID}

import csvLinkedInVisualizador
#csvLinkedInVisualizador.csvLinkedinLocais é um dic com as localizações do csv

#do linkedin num dictionary de elementos ID = {"latitude": latitudeID, "longitude" : longitudeID}

import pandas as pd
import numpy as np

import sys

#os allow us to manipulate dir, folders, files
import os
import os.path

from datetime import datetime
nowRaw = datetime.now()
now = str(nowRaw)

importCsv = csvLinkedInVisualizador.csvLinkedinLocais
importHdfs = hdfsWikipediaVisualizador.hdfsWikipediaLocal


csvLatitudeRow = []
csvLongitudeRow = []
csvLatitudeIntRow = []
csvLongitudeIntRow = []
csvIdRow = []
hdfsLatitudeRow = []
hdfsLongitudeRow = []

for i in range(1, len(importCsv)):
    csvLatitudeString = ""
    csvLongitudeString = ""
    csvIdString =""
    listCsv = importCsv[i]
    def isFloat(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    if(isFloat(listCsv["latitude"]) == True ): 
        if((float(listCsv["latitude"]) >= 10.0000) or (float(listCsv["latitude"]) <= -10.0000)):
            csvLatitudeString = str(listCsv["latitude"]).replace("-", "")
        else:
            csvLatitudeString = "0" + str(listCsv["latitude"]).replace("-", "")
        if((float(listCsv["longitude"]) >= 10.00000000) or (float(listCsv["longitude"]) <= 10.00000000)):
            csvLongitudeString = str(listCsv["longitude"]).replace("-", "")
        else:
            csvLongitudeString = "0" + str(listCsv["longitude"]).replace("-", "")
        if((len(csvLatitudeString) > 4) and (len(csvLatitudeString) > 4)):
            csvLatitudeIntRow = csvLatitudeIntRow + [len(csvLatitudeString)]
            csvLatitudeRow = csvLatitudeRow + [csvLatitudeString]
            csvLongitudeIntRow = csvLongitudeIntRow + [len(csvLongitudeString)]
            csvLongitudeRow = csvLongitudeRow + [csvLongitudeString]
            csvIdRow = csvIdRow + csvIdString

    
print('stop')
minLatitudeDef = min(csvLatitudeIntRow)
minLongitudeDef = min(csvLongitudeIntRow)
idMinimoLat = csvLatitudeIntRow.index(min(csvLatitudeIntRow))
print(idMinimoLat)
idMinimoLong = csvLongitudeIntRow.index(min(csvLongitudeIntRow))
print(idMinimoLong)
#for i in range(1, len(importHdfs)):
#    listHdfs = importHdfs[i]
#    hdfslatituderow = hdfslatituderow + [listHdfs["latitude"]]
#    hdfslongituderow = hdfslongituderow + [listHdfs["longitude"]]
print("latitude")
print(csvLatitudeRow[idMinimoLat], csvLongitudeRow[idMinimoLong], csvIdRow[idMinimoLong])
print("longitude")
print(csvLongitudeRow[idMinimoLong])
print(len(importHdfs))


#TODO criar pagina de log
save_path = './'
name_of_file = now +"StatPreview" ".txt"
completeName = os.path.join(save_path, name_of_file )
f = open(completeName, "w")

f.write("Log será adicionado futuramente")
f.write('\n\n\n\n')
f.write('-------------------------------------------------------------------------------------------\n')
 
f.close()