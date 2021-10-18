import requests



r = requests.get('https://www.wikidata.org/wiki/Q4')

print(r.text)