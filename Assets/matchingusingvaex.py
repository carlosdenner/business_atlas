import vaex
from IPython.display import display, HTML
import matplotlib
#from vaex.ui.colormaps import cm_plusmin
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os.path
import os
from datetime import datetime
import pandas as pd
import time



nowRaw = datetime.now()
nowStart = str(nowRaw)
print("started at " + nowStart)
df = vaex.open('../Databases/companies/output_chunk-*.csv')
print('vaex ate aqui')
df["Company_name"] = df["Company name"]
nomesLinkedin = df["Company_name"].str.lower().tolist()
lowerlink=[]

col_list2 = ["company"]
df2 = vaex.open("../Databases/tablehdfWikipedia/output_chunk-*.csv", usecols=col_list2)

print('nomeswiki')
print('foi')
counter = 2
   
   


print('começa funçaõ')
liste = df2["company"].str.lower().tolist()
print(liste)

print(liste)
print("aplicada")

time.sleep(200)




counter = 0
nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("wiki começou as " + wikiStart)
nomesWiki = df2["company"].str.lower().tolist()
print(nomesWiki)
print('foi')
lowerwiki=[]
#for industry in nomesWiki:
#    industry = str(industry).lower()
#    industryword = [industry]
#    lowerwiki = lowerwiki + industryword
#    counter = counter + 1
#    nowRaw = datetime.now()
#    wikiTime = str(nowRaw)
#    ratio = counter / len(nomesWiki)
#    if(counter % 1000 == 0):
#        print('foram ' + "{:.2f}".format(ratio) + "por cento, " + str(counter) + 'registros de ' + str(len(nomesWiki)) + "as " + wikiTime + " tendo começado as " + wikiStart)



nowRaw = datetime.now()
linkStart = str(nowRaw)
counter = 0
#print("LinkedIn começou as " + linkStart)
#for industry in nomesLinkedin:
#    industry = str(industry).lower()
#    industryword = [industry]
#    lowerlink = lowerlink + industryword
#    counter = counter + 1
#    nowRaw = datetime.now()
#    linkTime = str(nowRaw)
#    ratio = counter / len(nomesLinkedin)
#    if(counter % 1000 == 0):
#        print('foram ' + str(ratio) + " por cento, " + str(counter) + 'registros de ' + str(len(nomesLinkedin)) + "as " + linkTime + " tendo começado as " + linkStart)
#linkstring = ''.join(str(lowerlink))


nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("link encerrou as " + linkStart)



col_list2 = ["company"]
df2 = pd.read_csv("industries.csv", usecols=col_list2)
nomesWiki = df2["company"].tolist()

counter = 0
nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("wiki começou as " + wikiStart)
lowerwiki=[]
#for industry in nomesWiki:
#    industry = str(industry).lower()
#    industryword = [industry]
 #   lowerlink = lowerlink + industryword
#    lowerwiki = lowerwiki + industry
#    counter = counter + 1
#    nowRaw = datetime.now()
#    wikiTime = str(nowRaw)
#    ratio = counter / len(nomesWiki)
#    if(counter % 1000 == 0):
#        print('foram ' + "{:.2f}".format(ratio) + "por cento, " + str(counter) + 'registros de ' + str(len(nomesWiki)) + "as " + linkTime)

#wikistring = ''.join(str(lowerwiki))
#print(wikistring)

#nowRaw = datetime.now()
#wikiStart = str(nowRaw)
#print("wiki encerrou as " + wikiStart)

#z = set(nomesLinkedin).intersection(nomesWiki)
#print(z)
#save_path = './'
#name_of_file = "hdfsLinkedin"+ nowStart +  "StatPreview" ".txt"
#completeName = os.path.join(save_path, name_of_file )
#f = open(completeName, "w")

#f.write("Log será adicionado futuramente\n")
#f.write(stringToText)
#f.write('\n\n\n\n')
#interseccaoArr = z
#tamanhoInterseccao = 'a interseccao tem ' + str(len(z)) + 'empresas'
#print(tamanhoInterseccao)
#f.write(tamanhoInterseccao)
#f.write('\n-------------------------------------------------------------------------------------------\n')
#f.write('linkstring abaixo:\n')
#print("")
#f.write('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
#f.write('wikistring abaixo:\n')
#f = open('interseccao.txt', 'w')
#f.write(str(interseccaoArr))
#f.close()

 
#f.close()
nowRaw = datetime.now()
nowEnd = str(nowRaw)
print("ended at " + nowEnd)