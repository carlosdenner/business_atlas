import vaex
import matplotlib
#from vaex.ui.colormaps import cm_plusmin
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = vaex.open('./companies-on-linkedin.csv.hdf5')

localHdfsLinkedInDic = []
# Importing fields from hdfs
df["Total_employee_estimate"] = df["Total employee estimate"].astype('int')
df["Current_employee_estimate"] = df["Current employee estimate"].astype('int')
df["Year_founded"] = df["Year founded"].astype('int')
df['lower_range'] = df["Size range"].str.slice(start=0, stop=1)
df['upper_range'] = df["Size range"].str.slice(start=4, stop=6)

def city (locality):
        try:
            return str(locality.split(',')[0])
        except:
            return 'None'
def estate (locality):
    try:
        return str(locality.split(',')[1])
    except:
        return 'None'
def country (locality):
    try:
        return str(locality.split(',')[2])
    except:
        return 'None'

df['city'] = df["Locality"].apply(city)
df['estate'] = df["Locality"].apply(estate)
df['country'] = df["Locality"].apply(country)

#End of filed importing

#Basic descriptive statistics

print("mean current employee estimate: " + str(df.mean(df["Current employee estimate"])))

print("sample size:", df.count(), "mean # of employees:", df.mean(df.Total_employee_estimate))
print("\n", df.groupby(by='Industry', agg={'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate')}))
print("\n", df.groupby(by='Industry').agg({'Industry': 'count','Total_employee_estimate': ['mean', 'std']}))

#Drawing a chart 

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

years = [1900, 2013]
bins = 1000
counts_x = df.count(binby=df.Year_founded, limits=years, shape=bins)

plt.plot(np.linspace(years[0], years [1], bins), counts_x)
fig = plt.figure(np.linspace(years[0], years [1], bins), counts_x)
fig.savefig('plot1.png')





#Cleaning, scaling down


#exporting the dataframe
hdfsLinkedInLocal = localHdfsLinkedInDic
