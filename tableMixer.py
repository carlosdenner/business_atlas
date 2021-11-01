import hdfsWikipediaVisualizador
#hdfsWikipediaVisualizador.hdfsWikipediaLocal é um dic com as localizações do hdfs

#da wikipedia num dictionary de elementos ID = {"latitude": latitudeID, "longitude" : longitudeID}

import csvLinkedInVisualizador
#csvLinkedInVisualizador.csvLinkedinLocais é um dic com as localizações do csv

#do linkedin num dictionary de elementos ID = {"latitude": latitudeID, "longitude" : longitudeID}

import pandas as pd

import sys

#os allow us to manipulate dir, folders, files
import os
import os.path

from datetime import datetime

intersecction = []
list1 = csvLinkedInVisualizador.csvLinkedinLocais
list2 = hdfsWikipediaVisualizador.hdfsWikipediaLocal


for i in range(1, 2):
    print(list1[i])
    print(list2[i])
print("elementos da interseção: " + str(len(intersecction)))