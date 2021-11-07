import numpy as np 
import pandas as pd 
import plotly as py
import vaex
import matplotlib.pyplot as plt
import plotly.express as px
import os
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

dfInicial = vaex.open("../Databases/companies/output_chunk-*.csv")

dfCountriesTotal = vaex.open("../DataSetExtractions/countriesTotal.csv")



print("We have the following data sets:")
print(dfInicial.describe())

print("And so we built the following table:")
print(dfCountriesTotal.describe())

pandasDfCountriesTotal =  dfCountriesTotal.to_pandas_df()
print("Here's a sample of the data in the table:")
sample = dfCountriesTotal.head(3) 
countries = sample["Country"].tolist()
industries = sample["Industry"].tolist()
table = vaex.from_arrays(countries = countries, industries = industries)
print(table)

print('Countries with most industries, in number:')
maxInd = pandasDfCountriesTotal.nlargest(10, 'Industry')
countries = maxInd["Country"].tolist()
industries = maxInd["Industry"].tolist()
table = vaex.from_arrays(countries = countries, industries = industries)
print(table)

print("Wich in turn can be seen in the following graph")
labels = countries
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects = ax.bar(x - width/2, industries, width, label='Industries')
ax.set_ylabel('Industries')
ax.set_title('Countries with more industries')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.legend()
ax.bar_label(rects, padding=6)
fig.tight_layout()

plt.show()


print('Now, we can see countries by the mean_size of industries, descrescent:')
meanInd = pandasDfCountriesTotal.nlargest(10, 'mean_size')
countries = meanInd["Country"].tolist()
mean_size = meanInd["mean_size"].tolist()
table = vaex.from_arrays(countries = countries, mean_size = mean_size)
print(table)

print("Wich can generate the following view:")
print(pandasDfCountriesTotal.nlargest(10, 'mean_size'))
labels = countries
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects = ax.bar(x - width/2, mean_size, width, label='Industries')
ax.set_ylabel('Industries')
ax.set_title('Countries by the mean size of their industries')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.legend()
ax.bar_label(rects, padding=6)
fig.tight_layout()

plt.show()


print('Now, we can see countries by the max_size of industries, descrescent:')
maxSizeInd = pandasDfCountriesTotal.nlargest(10, 'max_size')
countries = maxSizeInd["Country"].tolist()
max_size = maxSizeInd["max_size"].tolist()
table = vaex.from_arrays(countries = countries, max_size = max_size)
print(table)

print("Wich can generate the following view:")
print(pandasDfCountriesTotal.nlargest(10, 'max_size'))
labels = countries
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects = ax.bar(x - width/2, max_size, width, label='Max size industries')
ax.set_ylabel('Industries')
ax.set_title('Countries by the max size of their industries')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.legend()
ax.bar_label(rects, padding=6)
fig.tight_layout()

plt.show()



#todo: prosseguir na descrição
#

DfCountriesTotal = vaex.from_pandas(df=pandasDfCountriesTotal, copy_index=True)
df_countries = DfCountriesTotal["Country"].tolist()
Industries = DfCountriesTotal["Industry"].tolist()




fig = go.Figure(data=go.Choropleth(
    locations = df_countries,
    locationmode = 'country names',
    z = Industries,
    colorscale = 'Reds',
    marker_line_color = 'black',
    marker_line_width = 0.5,
))

print('And here we can see the density of companies in the world:')
fig.show()

print("Here we will see the same map, but removing united states and uk from the list:")

usaIndex = df_countries.index("united states")
Industries.remove(max(Industries))
Industries.remove(max(Industries))
df_countries.remove("united states")
df_countries.remove("united kingdom")

fig = go.Figure(data=go.Choropleth(
    locations = df_countries,
    locationmode = 'country names',
    z = Industries,
    colorscale = 'Reds',
    marker_line_color = 'black',
    marker_line_width = 0.5,
))

fig.show()
#fig.update_layout(
#    title_text = 'Confirmed Cases as of March 28, 2020',
#    title_x = 0.5,
#    geo=dict(
#        showframe = False,
#        showcoastlines = False,
#        projection_type = 'equirectangular'
#3    )
#)


#df_countrydate = df[df['Confirmed']>0]
#df_countrydate = df_countrydate.groupby(['Date','Country']).sum().reset_index()
#df_countrydate

#fig = px.choropleth(df_countrydate, 
#                    locations="Country", 
#                    locationmode = "country names",
#                    color="Confirmed", 
#                    hover_name="Country", 
#                    animation_frame="Date"
#                   )
#fig.update_layout(
#    title_text = 'Global Spread of Coronavirus',
#    title_x = 0.5,
#    geo=dict(
#        showframe = False,
#        showcoastlines = False,
#    ))
    
#fig.show()