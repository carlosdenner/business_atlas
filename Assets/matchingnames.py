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



nowRaw = datetime.now()
nowStart = str(nowRaw)
print("started at " + nowStart)
col_list = ["Company_name"]
df = pd.read_csv("nameslinkedin.csv", usecols=col_list)
nomesLinkedin = df["Company_name"].tolist()
lowerlink=[]

col_list2 = ["company"]
df2 = pd.read_csv("industries.csv", usecols=col_list2)
nomesWiki = df2["company"].tolist()

counter = 0
nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("wiki começou as " + wikiStart)
lowerwiki=[]
for industry in nomesWiki:
    industry = str(industry).lower()
    industryword = [industry]
    lowerwiki = lowerwiki + industryword
    counter = counter + 1
    nowRaw = datetime.now()
    wikiTime = str(nowRaw)
    ratio = counter / len(nomesWiki)
    print('foram ' + "{:.2f}".format(ratio) + "por cento, " + str(counter) + 'registros de ' + str(len(nomesWiki)) + "as " + wikiTime + " tendo começado as " + wikiStart)



nowRaw = datetime.now()
linkStart = str(nowRaw)
counter = 0
print("LinkedIn começou as " + linkStart)
for industry in nomesLinkedin:
    industry = str(industry).lower()
    industryword = [industry]
    lowerlink = lowerlink + industryword
    counter = counter + 1
    nowRaw = datetime.now()
    linkTime = str(nowRaw)
    ratio = counter / len(nomesLinkedin)
    print('foram ' + str(ratio) + " por cento, " + str(counter) + 'registros de ' + str(len(nomesLinkedin)) + "as " + linkTime + " tendo começado as " + linkStart)
linkstring = ''.join(str(lowerlink))


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
for industry in nomesWiki:
    industry = str(industry).lower()
    industryword = [industry]
    lowerlink = lowerlink + industryword
    lowerwiki = lowerwiki + industry
    counter = counter + 1
    nowRaw = datetime.now()
    wikiTime = str(nowRaw)
    ratio = counter / len(nomesWiki)
    print('foram ' + "{:.2f}".format(ratio) + "por cento, " + str(counter) + 'registros de ' + str(len(nomesWiki)) + "as " + linkTime)

wikistring = ''.join(str(lowerwiki))
print(wikistring)

nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("wiki encerrou as " + wikiStart)

z = set(nomesLinkedin).intersection(nomesWiki)
print(z)
save_path = './'
name_of_file = "hdfsLinkedin"+ nowStart +  "StatPreview" ".txt"
completeName = os.path.join(save_path, name_of_file )
f = open(completeName, "w")

f.write("Log será adicionado futuramente\n")
#f.write(stringToText)
f.write('\n\n\n\n')
interseccaoArr = z
tamanhoInterseccao = 'a interseccao tem ' + str(len(z)) + 'empresas'
print(tamanhoInterseccao)
f.write(tamanhoInterseccao)
f.write('\n-------------------------------------------------------------------------------------------\n')
f.write('linkstring abaixo:\n')
print("")
f.write('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
f.write('wikistring abaixo:\n')
f = open('interseccao.txt', 'w')
f.write(str(interseccaoArr))
f.close()

 
f.close()
nowRaw = datetime.now()
nowEnd = str(nowRaw)
print("ended at " + nowEnd)