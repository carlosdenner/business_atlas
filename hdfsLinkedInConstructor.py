import vaex
import matplotlib
#from vaex.ui.colormaps import cm_plusmin
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = vaex.open(r'./companies-on-linkedin.csv.hdf5')
df.show_batch()
print(df.info())
#Cleaning, scaling down


