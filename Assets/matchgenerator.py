import re
import os
from datetime import datetime




f = open("hdfsLinkedin2021-10-06 08:19:03.816962StatPreview.txt", "r")

nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("abriu arquivo " + wikiStart)

line = f.read()
line = line.lower()
line = re.sub(']', '', line)

nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("tirou o ] " + wikiStart)


lines = line.split('\n')
print(str(len(lines)))

g = open('setInterseccao.txt', 'w')
def linecleaner(line):
    print("original: " + str(len(line)))
    listaa = line.split(',')
    print(len(listaa))
    counter = 0
    for item in listaa:
        if len(item) <= 1:
            item = ''
    print("itens de compriemnto 1 :" + str(counter))
    #print(line)
    return listaa
linhalimpa1 = linecleaner(lines[1])
linhalimpa2 = linecleaner(lines[3])
nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("splitou as lista " + wikiStart)
z = set(linhalimpa1).intersection(linhalimpa2)
nowRaw = datetime.now()
wikiStart = str(nowRaw)
print("calculou intersecção " + wikiStart)
print(z)
print(len(z))
g.write(str(z))
g.close()
f.close()

