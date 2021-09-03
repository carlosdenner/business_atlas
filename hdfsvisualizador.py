import sys
from SPARQLWrapper import SPARQLWrapper, JSON

#os allow us to manipulate dir, folders, files
import os
import os.path

from datetime import datetime


endpoint_url = "https://query.wikidata.org/sparql"



query = """#List of `instances of` "business enterprise"
SELECT ?com ?comLabel ?inception ?industry ?industryLabel ?coordinate ?country WHERE {
  ?com (wdt:P31/(wdt:P279*)) wd:Q4830453;
    wdt:P625 ?coordinate.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
  OPTIONAL { ?com wdt:P571 ?inception. }
  OPTIONAL { ?com wdt:P452 ?industry. }
  OPTIONAL { ?com wdt:P17 ?country. }
}"""


def get_results(endpoint_url, query):
    user_agent = "Business_atlas Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


#results = get_results(endpoint_url, query)

#for result in results["results"]["bindings"]:
    #print(result)



import json
import pandas as pd
from pandas.io.json import json_normalize

filename = 'tablehdf.h5'

######-This session retireves data form the sources

# Get the dataset, and transform string into floats for plotting
#dataFrame = pd.json_normalize(results["results"]["bindings"])  # in a serialized json-based format
#df = pd.DataFrame(dataFrame)  # into pandas

#p = r'(?P<latitude>-?\d+\.\d+).*?(?P<longitude>-?\d+\.\d+)'  # get lat/lon from string coordinates
#df[['longitude', 'latitude']] = df['coordinate.value'].str.extract(p, expand=True)

#df['latitude'] = pd.to_numeric(df['latitude'], downcast='float')
#df['longitude'] = pd.to_numeric(df['longitude'], downcast='float')


######-End of retrieving session

######-This session buildis the store for the first time

#data = pd.DataFrame(df, columns=['latitude', 'longitude', 'comLabel.value', 'coordinate.value', 'inception.value',
#                                'industryLabel.value', 'com.value', 'industry.value', 'country.value',
#                                 'countryLabel.value'])
#data2 = pd.DataFrame(df, columns =[])
#data = data.dropna(subset=['latitude', 'longitude'])
#data.rename(columns={'comLabel.value': 'company'}, inplace=True)
#data.rename(columns={'coordinate.value': 'coordinate'}, inplace=True)
#data.rename(columns={'inception.value': 'inception'}, inplace=True)
#data.rename(columns={'industryLabel.value': 'industry'}, inplace=True)
#data.rename(columns={'com.value': 'id'}, inplace=True)
#data.rename(columns={'industry.value': 'id_industry'}, inplace=True)
#data.rename(columns={'country.value': 'id_country'}, inplace=True)
#data.rename(columns={'countryLabel.value': 'country'}, inplace=True)
#data = pd.DataFrame(data)  # cluster maps works ONLY with dataframe

######-End of building session


######-This session will implement an append method to add data to the dataset
#store = pd.HDFStore(filename)
#store.append('data', data)
#store.close()

nowRaw = datetime.now()
now = str(nowRaw)


store = pd.HDFStore("tablehdf.h5")
save_path = './'
name_of_file = now +"StatPreview" ".txt"
completeName = os.path.join(save_path, name_of_file )
f = open(completeName, "w")
f.write("there is somthign in the air tonight")
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
for row in df.itertuples():
    allsum = allsum + float(row.Index)
print(allsum)
df.info()
print(df.sample(5))