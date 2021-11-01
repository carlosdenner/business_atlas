#Main data extractor from linkedin datasource
#generates the following views on linkedIn data:
#
#1-countriestotal.csv
#A view containing aggregate information about each country:
#
#Country, Industry, Total_employee_estimate_mean,
# Total_employee_estimate_std, mean_size, max_size
#
#2-industriesTotal.csv
#
#A view containing aggregate information about each industry sector:
#
#Industry,Country,Total_employee_estimate_mean,Total_employee_estimate_std,
# mean_size,max_size
#
#3-LinkedInH5IndustryCountry
#
#Company name,Company URL domain,Year founded,Industry,Size range,Locality,
# Country,Linkedin URL,Current employee estimate,Total employee estimate,
# Total_employee_estimate,Country_Only,Current_employee_estimate,Year_founded,
# lower_range,Company_name,Company_URL_Domain,upper_range,CountryNotNull,
# CountryxInd




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

#log creation, to store info about the proccess
nowRaw = datetime.now()
nowStart = str(nowRaw)
nowBegin = nowStart
save_path = '../Logs/'
name_of_file = "hdfsLinkedin" + "StatPreview" ".txt"
completeName = os.path.join(save_path, name_of_file )
log = open(completeName, "a")

log.write("Info about dataExtraction:\n")
log.write("Started analysis at " + nowStart + "")


print("Started analysis at " + nowStart)


df = vaex.open('../Databases/companiesOnLinkedin/output_chunk-*.csv')

dbSize = os.path.getsize('../Databases/companiesOnLinkedin')
log.write("\n\nDatabase size: " + str(dbSize))
log.write("\n# of lines: " + str(df.count()))


# Importing fields from hdfs
print("Data imported")
df["Total_employee_estimate"] = df["Total employee estimate"].astype('int')
df["Country_Only"] = df["Country"]
df["Current_employee_estimate"] = df["Current employee estimate"].astype('int')
df["Year_founded"] = df["Year founded"].astype('int')
df['lower_range'] = df["Size range"].str.slice(start=0, stop=1)
df['Company_name'] = df['Company name']
df['Company_URL_Domain'] = df['Company URL domain']
df['upper_range'] = df["Size range"].str.slice(start=4, stop=6)
nowRaw = datetime.now()
nowstr = str(nowRaw)
log.write("\n\n\nColumns generated at: " + nowstr)
print("Columns generated")
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


df["CountryNotNull"] = df["Country"].str.byte_length() > 0

print(df.count(df["CountryNotNull"] == True))

#creating an column to make some operations between country and industry 
#sectors
df.add_virtual_column("CountryxInd", df["Country"] + ", " + df["Industry"])


df2 = df["Industry"].values
describeAfter = df.describe()
#Basic descriptive statistics
#print("\n Correlation between total and current number of employees: \n" + str(df.correlation("Total_employee_estimate", "Current_employee_estimate")))
#print("\n Correlation between Year_founded and current number of employees: \n" + str(df.correlation("Year_founded", "Current_employee_estimate")))
#print("\n Correlation between Year_founded and total number of employees: \n" + str(df.correlation("Year_founded", "Total_employee_estimate")))
#print("mean current employee estimate: " + str(df.mean(df["Current employee estimate"])))
#print("\n Correlation between total and Year_founded: \n" + str(df.correlation("Total_employee_estimate", "Year_founded")))
#print("\n", df.groupby(by='Locality', agg={'number of industries': 'count','Current employee estimate': ['mean', 'std']}))
#print('--------------------------------------------')

#SMALL_SIZE = 12
#MEDIUM_SIZE = 14
#BIGGER_SIZE = 16

#plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
#plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
#plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
#plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
#plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
#plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#years = [1900, 2013]
#bins = 1000
#counts_x = df.count(binby=df.Year_founded, limits=years, shape=bins)
#counts_x

#plt.plot(np.linspace(years[0], years [1], bins), counts_x)

#plt.write_html("industriesby.html")
#plt.savefig('industries_by_year.jpg')
#print('--------------------------------------------')
#print("sample size:", df.count(), "mean # of employees:", df.mean(df["Total_employee_estimate"]))
#print("\n", df.groupby(by='Industry', agg={'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate'), }))
#print("\n", df.groupby(by='Industry'), agg={'Industry': 'count','Total_employee_estimate': ['mean', 'std']}, agg={'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate'), })

nowRaw = datetime.now()
nowStart = str(nowRaw)
CountriesTotal = df.groupby(by='Country', agg={'Industry': 'count','Total_employee_estimate': ['mean', 'std'], 'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate')} )
CountriesTotal.export_csv('../DataSetExtractions/countriesTotal.csv')
print("exported CountriesTotal")
countriesDbSize = str(os.path.getsize('../DataSetExtractions/countriesTotal.csv'))
log.write("\n\n\nCountries data size: " + countriesDbSize)
log.write("\n# of lines in countries: " + str(CountriesTotal.count()))
nowRaw = datetime.now()
nowEnd = str(nowRaw)
log.write("\ncountriesTotal.csv building started at: " + nowStart)
log.write("\ncountriesTotal.csv building endeded at: " + nowEnd)



nowRaw = datetime.now()
nowStart = str(nowRaw)
industriesTotal = df.groupby(by='Industry', agg={'Country': 'count','Total_employee_estimate': ['mean', 'std'], 'mean_size': vaex.agg.mean('Current_employee_estimate'), 'max_size': vaex.agg.max('Current_employee_estimate')} )
industriesTotal.export_csv('../DataSetExtractions/industriesTotal.csv')
industriesDbSize = str(os.path.getsize('../DataSetExtractions/industriesTotal.csv'))
log.write("\n\n\nIndustries data size: " + industriesDbSize)
log.write("\n# of lines in industries: " + str(industriesTotal.count()))
nowRaw = datetime.now()
nowEnd = str(nowRaw)
log.write("\nindustriesTotal.csv building started at: " + nowStart)
log.write("\nindustriesTotal.csv building endeded at: " + nowEnd)


dfInd = df[df.CountryxInd.str.len() > 0]

print(dfInd.count())
nowRaw = datetime.now()
nowStart = str(nowRaw)
dfInd.export_hdf5('../DataSetExtractions/LinkedInH5IndustryCountry.hdf5')
dfIndDbSize = str(os.path.getsize('../DataSetExtractions/LinkedInH5IndustryCountry.hdf5'))
log.write("\n\n\nIndustries data size: " + dfIndDbSize)
log.write("\n# of lines in industries: " + str(dfInd.count()))
log.write("\nLinkedInH5IndustryCountry.hdf5 building started at: " + nowStart)
log.write("\nLinkedInH5IndustryCountry.hdf5 building endeded at: " + nowEnd)







log.write("\n\nStarted analysis at " + nowBegin)
log.write("\nAnalisys ended at " + nowEnd)
log.write('\n\n\n\n')

 
log.close()
#print(samplestring )





#Cleaning, scaling down


#exporting the dataframe


