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

query = """#List of `instances of` "Country codes"
SELECT ?country ?label_en  {
    ?country wdt:P31 wd:Q6256.
    ?country rdfs:label ?label_en filter (lang(?label_en) = "en").
}"""
def get_results(endpoint_url, query):
    user_agent = "Business_atlas Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)


# PUT THE DATA ON THE RIGHT FORMAT into pandas


# Get the dataset, and transform string into floats for plotting
dataFrame = pd.json_normalize(results["results"]["bindings"])
print(dataFrame)
dataFrame.to_csv("entitiesAndCountries.csv")
del dataFrame['country.type']
del dataFrame['label_en.xml:lang']
del dataFrame['label_en.type']

datathin = dataFrame.copy(["label_en.value", "country.value"])
#datathin = datathin.drop(country.type")
print(datathin)
datathin.to_csv("datathi.csv")