import re

from string import punctuation

from datetime import datetime

datahora = str(datetime.now())
print(datahora)
datafim = ''.join(ch for ch in datahora if ch.isalnum())
print(datafim)
print(punctuation)
