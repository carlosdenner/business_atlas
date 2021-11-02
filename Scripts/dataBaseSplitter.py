#This utility takes an big dataBase and uses Vaex to split it on small data
#chunks, so it can be easily handed(since some architectures can't handle 
# big files).

import vaex
import numpy as np
import os
import pandas
from datetime import datetime

nowRaw = datetime.now()
nowStart = str(nowRaw)

df = vaex.open('../DataSetExtractions/timecountryindustry/timecountryindustry.csv')

print(df.head(3))
print('começou o exporte na globo as ' + nowStart)
df.export_many('../DataSetExtractions/timecountryindustry/output_chunk-{i:02}.csv', chunk_size=10_000)