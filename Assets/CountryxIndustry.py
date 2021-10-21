import pandas
import vaex
import os
from datetime import datetime
import numpy as np
import json
import csv


print('1st break')
dataCountries = pandas.read_csv('../DataSetExtractions/countriesTotal.csv')
dataInd = pandas.read_csv('../DataSetExtractions/industriesTotal.csv')
datamix = vaex.open('../DataSetExtractions/LinkedInH5IndustryCountry.hdf5')
print("second break")
print(datamix.head(3))
#Mocking tests
listnum = ['d', 'e', 'f', 'g']
listalph = ['a', 'b', 'c']
listMAtrix = ['d,a', 'e,c', 'e,c', 'e,a']
#end mocking tests
countries = dataCountries.Country.tolist()
print('third break')
ind = dataInd.Industry.tolist()
print('4th break')
ind.pop()
print('-----------------------------------')
countryxInd = datamix["CountryxInd"].tolist()
print('\n\n\n\n\n\n\n\n-----------------')
#print(countryxInd)
print('\n\n\n\n\n\n\n\n-----------------')


def matrixer(list1, list2):
    listGen = {}
    for item in list1:
        for anotheritem in list2:
            verb = str(item) + ', ' + str(anotheritem)
            listGen[verb] = 0
    return listGen

#
print("5th break")
matrixCI = matrixer(countries, ind)
print(matrixCI)
list = countryxInd

def matrixCount(list, matrix):
    countBad = 0
    for item in list:
        try:
            matrix[item] += 1
        except:
            print('bad')
            countBad += 1
    print(countBad)
    return matrix
print("8th break")
matrixdict = matrixCount(countryxInd, matrixCI)
print(matrixdict)



with open('../DataSetExtractions/Countryxindustry.csv','w') as f:
    w = csv.writer(f)
    w.writerows(matrixdict.items())
