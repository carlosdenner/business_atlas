# ASK WIKIPEDIA FOR LIST OF COMPANIES
# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

import os.path
import os
import json
import pandas as pd
from pandas.io.json import json_normalize


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


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)

# PUT THE DATA ON THE RIGHT FORMAT into pandas


# Get the dataset, and transform string into floats for plotting
dataFrame = pd.json_normalize(results["results"]["bindings"])  # in a serialized json-based format
df = pd.DataFrame(dataFrame)  # into pandas
p = r'(?P<latitude>-?\d+\.\d+).*?(?P<longitude>-?\d+\.\d+)'  # get lat/lon from string coordinates
df[['longitude', 'latitude']] = df['coordinate.value'].str.extract(p, expand=True)
df['latitude'] = pd.to_numeric(df['latitude'], downcast='float')
df['longitude'] = pd.to_numeric(df['longitude'], downcast='float')
data = pd.DataFrame(df, columns=['latitude', 'longitude', 'comLabel.value', 'coordinate.value', 'inception.value',
                                 'industryLabel.value', 'com.value', 'industry.value', 'country.value',
                                 'countryLabel.value'])
data2 = pd.DataFrame(df, columns =[])
data = data.dropna(subset=['latitude', 'longitude'])
data.rename(columns={'comLabel.value': 'company'}, inplace=True)
data.rename(columns={'coordinate.value': 'coordinate'}, inplace=True)
data.rename(columns={'inception.value': 'inception'}, inplace=True)
data.rename(columns={'industryLabel.value': 'industry'}, inplace=True)
data.rename(columns={'com.value': 'id'}, inplace=True)
data.rename(columns={'industry.value': 'id_industry'}, inplace=True)
data.rename(columns={'country.value': 'id_country'}, inplace=True)
data.rename(columns={'countryLabel.value': 'country'}, inplace=True)
data = pd.DataFrame(data)  # cluster maps works ONLY with dataframe

#saving hdf
filename = 'tablehdfWikipedia.h5'
store = pd.HDFStore(filename)
store.append('data', data)
store.close()

store = pd.HDFStore(filename)

sample = store['data']

print(sample)
store.close()

data.to_hdf(filename, 'data', mode='w', format='table')

del df    # allow df to be garbage collected




