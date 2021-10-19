import numpy as np
import vaex
import pandas as pd
import matplotlib.pyplot as plt

import geopandas


world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))

print('world head')
headWorld = world.head()
headWorld.to_csv("headworld")
print(world.head())
print('----cities head----')

headcities = cities.head()
headcities.to_csv("headcities")
print(cities.head())
print("salvando o mundo")
figWorld = world.plot().get_figure().savefig('output.png')
print('salvando townsville')
figCities = cities.plot().get_figure().savefig('output2.png')

