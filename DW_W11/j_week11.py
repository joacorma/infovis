import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

dataUrl = 'https://query.data.world/s/bu3wd65ba7eidffud6gee3l72wklk5'
title = '2020/W11: Self-reported Life Satisfaction vs GDP per capita'
x_label = 'GDP'
y_label = 'Life satisfaction'

df = pd.read_csv(dataUrl)
regionsExcel = pd.read_excel('https://query.data.world/s/yu2uk6plt66axdmwxnailqrj2ni3sx')
joined = df.join(regionsExcel.set_index('Country'), on='Entity')
year = 2017

#0 Entity - Country
#2 Year - Year
#3 GDP per capita (constant 2011 international $) - GDP
#4  Life satisfaction (country average; 0-10) (Cantril Ladder (0=worst; 10=best)) - Life Satisf
#5 Unnamed - Population

cleaned = joined.dropna()

fig = go.Figure()

##SLIDER - Hay que buscar otra forma porque son demasiados datos cargados juntos
    # for year in np.arange(np.min(cleaned['Year']), np.max(cleaned['Year'])+1):
    #     year_bool = cleaned['Year'] == year
    #     yeared = cleaned[year_bool]

    #     #print(yeared)

    #     country = yeared.iloc[:,0]
    #     gdp = yeared.iloc[:,3]
    #     satisfaction = yeared.iloc[:,4]
    #     popul = yeared.iloc[:,5]
    #     region = yeared.iloc[:,6]

    #     fig.add_trace(
    #         go.Scatter(
    #                 visible=False,
    #                 mode='markers',
    #                 name="𝜈 = " + str(year),
    #                 x=gdp,
    #                 y=satisfaction,
    # #                marker=dict(size=popul),
    # #                marker_color=region,
    #                 text=country))

    # # Make 10th trace visible
    # fig.data[10].visible = True

    # # Create and add slider
    # steps = []
    # for i in range(len(fig.data)):
    #     step = dict(
    #         method="restyle",
    #         args=["visible", [False] * len(fig.data)],
    #     )
    #     step["args"][1][i] = True  # Toggle i'th trace to "visible"
    #     steps.append(step)

    # sliders = [dict(
    #     active=10,
    #     currentvalue={"prefix": "Year: "},
    #     pad={"t": 50},
    #     steps=steps
    # )]
    

#BASICO
year_bool = cleaned['Year'] == year
yeared = cleaned[year_bool]

#print(yeared)

country = yeared.iloc[:,0]
gdp = yeared.iloc[:,3]
satisfaction = yeared.iloc[:,4]
popul = yeared.iloc[:,5]
region = yeared.iloc[:,6]

fig = px.scatter(df, x=gdp, y=satisfaction,
                 size=popul, hover_name=country, color=region, labels={'x':x_label, 'y':y_label, 'color':'Regions'})

fig.update_layout(title=title)
#fig.update_layout(title=title, sliders=sliders)

fig.show()
