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



print("Os dados foram extraídos dos seguintes conjuntos de dados:")
print(dfInicial.describe())

print("Gerando a seguinte tabela:")
print(dfCountriesTotal.describe())

pandasDfCountriesTotal =  dfCountriesTotal.to_pandas_df()
print("Amostra dos dados presentes no dataset, após agruparmos as empresas por país:")
print(dfCountriesTotal.head(3)) 

print('Países com maior número total de indústrias:')
print(pandasDfCountriesTotal.nlargest(10, 'Industry'))


print('Países com maior tamanho médio de indústrias:')
print(pandasDfCountriesTotal.nlargest(10, 'mean_size'))

print('Países com maior tamanho máximo de indústrias:')
print(pandasDfCountriesTotal.nlargest(10, 'max_size'))


#todo: prosseguir na descrição
#

DfCountriesTotal = vaex.from_pandas(df=pandasDfCountriesTotal, copy_index=True)
df_countries = DfCountriesTotal["Country"].tolist()
Industries = DfCountriesTotal["Industry"].tolist()


print(type(df_countries))


fig = go.Figure(data=go.Choropleth(
    locations = df_countries,
    locationmode = 'country names',
    z = Industries,
    colorscale = 'Reds',
    marker_line_color = 'black',
    marker_line_width = 0.5,
))

print('Exibição de um mapa:')
fig.show()

print("Impressão do mapa")
fig.write_html(file='maostat.html')
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