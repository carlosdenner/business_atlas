import requests
import os.path
import os

from datetime import datetime

nowRaw = datetime.now()
nowStart = str(nowRaw)
print("op começou as " + nowStart)

for i in range(1, 500):
    print("item " + str(i) +  " buscado.")
    entity = 'https://www.wikidata.org/wiki/Q' + str(i)
    r = requests.get(entity)
    line = r.text
    lineForm = line[101:140]
    lineForm = "item " + str(i) + ": " + lineForm 
    print(lineForm)
    lineForm = lineForm + ',\n'
    f = open("wiki.txt", "a")
    f.write(lineForm)
f.close()
nowRaw = datetime.now()
nowStart = str(nowRaw)
print("op cabou  as " + nowStart)