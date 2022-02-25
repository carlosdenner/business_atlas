# This script makes a request on wikipedia, retrieves information
#about the companies in there and store these data in a 
#hdfs file for further analysis
import sys
import requests
import pandas as pd
import json
import pprint
import seaborn as sns
import matplotlib.pyplot as plt
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

query = """#List of `instances of` "countries"
SELECT ?country ?countryLabel ?gdp ?currencyLabel ?flag (count(*) as ?rank) WHERE {
#  values ?country {wd:Q30 wd:Q184}
  ?country wdt:P463 wd:Q37470. 
  ?country2 wdt:P463 wd:Q37470.          
  ?country p:P2131 [ psv:P2131 [ wikibase:quantityAmount ?gdp; wikibase:quantityUnit ?currency ]; pq:P585 ?time; prov:wasDerivedFrom/pr:P248 wd:Q21540096 ] .
  FILTER(YEAR(?time) = 2017) .
  SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' }
  ?country2 p:P2131 [ psv:P2131 [ wikibase:quantityAmount ?gdp2; wikibase:quantityUnit ?currency ]; pq:P585 ?time; prov:wasDerivedFrom/pr:P248 wd:Q21540096 ] .
  filter (?gdp2 >= ?gdp)
  ?country wdt:P41 ?flag.
} group by ?country ?countryLabel ?gdp ?currencyLabel ?flag ORDER BY ?rank"""

data = []

def get_results(endpoint_url, query):
    user_agent = "Business_atlas Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)


dataFrame = pd.json_normalize(results["results"]["bindings"])  # in a serialized json-based format
df = pd.DataFrame(dataFrame)

print(df.describe())
df.to_csv("df.csv")
#,country.type,country.value,countryLabel.xml:lang,countryLabel.type,countryLabel.value,alpha2.type,alpha2.value,alpha3.type,alpha3.value,pop.datatype,pop.type,pop.value,gdp.datatype,gdp.type,gdp.value,callingCode.type,callingCode.value,drivingSideLabel.xml:lang,drivingSideLabel.type,drivingSideLabel.value,tlds.type,tlds.value,timezones.type,timezones.value,continents.type,continents.value,currencies.type,currencies.value,voltages.type,voltages.value,frequencies.type,frequencies.value,plugTypes.type,plugTypes.value,capitals.type,capitals.value
data = pd.DataFrame(df, columns=['countryLabel.value', 'gdp.value', 'countryLabel.value',
                                 'pop.value'])
print(data.describe())
data.to_csv("df.csv")
#for response in response_list['data']:
#    popData = response.get('populationCounts')
#    popValue = popData[-1].get('value')
#    data.append({
#        "city": response.get('city'),
#        "country": response.get('country'),
#        "population": popValue,        
#    })
#print(data)