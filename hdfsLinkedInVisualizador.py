import vaex
from IPython.display import display, HTML
import matplotlib
#from vaex.ui.colormaps import cm_plusmin
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os.path
import os
from datetime import datetime
import nominatintest as nominatim

nowRaw = datetime.now()
nowStart = str(nowRaw)
print("op começou as " + nowStart)


df = vaex.open('./companies-on-linkedin.csv.hdf5')
print("leu o hdf5")
csvSample = df.head(2)
csvSample.export_csv('./head.csv')
localHdfsLinkedInDic = []
# Importing fields from hdfs
print("gerou head.csv")
df["Total_employee_estimate"] = df["Total employee estimate"].astype('int')
df["Country_Only"] = df["Country"]
df["Current_employee_estimate"] = df["Current employee estimate"].astype('int')
df["Year_founded"] = df["Year founded"].astype('int')
df['lower_range'] = df["Size range"].str.slice(start=0, stop=1)
df['Company_name'] = df['Company name']
df['Company_URL_Domain'] = df['Company URL domain']
df['upper_range'] = df["Size range"].str.slice(start=4, stop=6)

print("gerou as coluna")
#df.select(df.x < 0)

#def city (locality):
#        try:
#            return str(locality.split(',')[0])
#        except:
#            return 'None'
#def estate (locality):
#    try:
#        return str(locality.split(',')[1])
#    except:
#        return 'None'
#def country (locality):
#    try:
#        return str(locality.split(',')[2])
#    except:
#        return 'None'

#df['city'] = df["Locality"].apply(city)
#df['estate'] = df["Locality"].apply(estate)
#df['country'] = df["Locality"].apply(country)

print("gerou as coluna")
print('todos ind')
print(df.count(df["Country_Only"]))
df["CountryNotNull"] = df["Country"].str.byte_length() > 0
print("ind com paises:")
print(df.count(df["CountryNotNull"] == True))
print("fazendo join pais industria")
df.add_virtual_column("countryxInd", df["Country"] + ", " + df["Industry"])
indcountryTable = []
def indCountryTMaker(industry, country):
    indcountryTable[industry, country] += 1
    print(industry + country)
    print(indcountryTable[industry, country])
print("fazendo a tabela pais/industria")
df.apply(indCountryTMaker, arguments=[df.Industry, df.Country])
print(indcountryTable)
print("tabela ai")
print("join aparentemente deu certo")
print('-.-.-.-.--.-.-.-..--------')
print(df.describe())
print("before drop country")
describeBefore = df.describe()
describeBefore.to_csv("./DropNacountrytestbefore.csv")

df2 = df["Industry"].values
print("------>>>>>>>>>------------")
#End of filed importing
print("after dropping country")
describeAfter = df.describe()
describeAfter.to_csv("./DropNacountrytestafter.csv")
#df2.to_csv("./df2.csv")
#Basic descriptive statistics
#print("\n Correlation between total and current number of employees: \n" + str(df.correlation("Total_employee_estimate", "Current_employee_estimate")))
#print("\n Correlation between Year_founded and current number of employees: \n" + str(df.correlation("Year_founded", "Current_employee_estimate")))
#print("\n Correlation between Year_founded and total number of employees: \n" + str(df.correlation("Year_founded", "Total_employee_estimate")))
#print("mean current employee estimate: " + str(df.mean(df["Current employee estimate"])))
#print("\n Correlation between total and Year_founded: \n" + str(df.correlation("Total_employee_estimate", "Year_founded")))
#print("\n", df.groupby(by='Locality', agg={'number of industries': 'count','Current employee estimate': ['mean', 'std']}))
#print('--------------------------------------------')

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
counts_x

plt.plot(np.linspace(years[0], years [1], bins), counts_x)
print("gerou grafico")
#plt.write_html("industriesby.html")
#plt.savefig('industries_by_year.jpg')
#print('--------------------------------------------')
#print("sample size:", df.count(), "mean # of employees:", df.mean(df["Total_employee_estimate"]))
#print("\n", df.groupby(by='Industry', agg={'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate'), }))
#print("\n", df.groupby(by='Industry'), agg={'Industry': 'count','Total_employee_estimate': ['mean', 'std']}, agg={'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate'), })
dftest = df.groupby(by='Country', agg={'Industry': 'count','Total_employee_estimate': ['mean', 'std'], 'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate')} )
print("criou dftest1")
dftest2 = df.groupby(by='Industry', agg={'Country': 'count','Total_employee_estimate': ['mean', 'std'], 'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate')} )

print("criou dftest2")


dftest.export_csv('./countriesTotal.csv')
print("exportou dftest1")


dftest2.export_csv('./industriesTotal.csv')
print("exportou dftest2 ")
dfSample = df.head(1000)
dfSample.export_csv('./linkedincsvindustrycuntry.csv')
print("criou dftest3")


#dftest3.export_csv('./matchesindcountryTotal.csv')
print("exportou dftest2 ")
#save_path = './'
#name_of_file = "hdfsLinkedin"+ nowStart +  "StatPreview" ".txt"
#completeName = os.path.join(save_path, name_of_file )
#f = open(completeName, "w")

#f.write("Log será adicionado futuramente\n")
#f.write(stringToText)
#f.write('\n\n\n\n')
#f.write('-------------------------------------------------------------------------------------------\n')
 
#f.close()



#Drawing a chart 


save_path = './'
name_of_file = "hdfsLinkedin"+ nowStart +  "StatPreview" ".txt"
completeName = os.path.join(save_path, name_of_file )
f = open(completeName, "w")

f.write("Log será adicionado futuramente\n")
#f.write(stringToText)
f.write('\n\n\n\n')
f.write('-------------------------------------------------------------------------------------------\n')
 
f.close()
#print(samplestring )





#Cleaning, scaling down


#exporting the dataframe
nowRaw = datetime.now()
nowEnds = str(nowRaw)
print(nowEnds)
hdfsLinkedInLocal = localHdfsLinkedInDic
